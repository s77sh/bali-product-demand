"""Keep this repo anonymous.

    python3 tools/anonymize.py --fix      rewrite text and file names in place (tracked and untracked, never ignored files)
    python3 tools/anonymize.py --check    exit 1 if any identifying term is left (used by the git hooks)
    python3 tools/anonymize.py --check-msg FILE    check a commit message

The terms live outside the repo, in ~/.config/anon-scrub/terms.json, so the list itself is never published.
Without that file, --check fails closed: nothing can be committed or pushed.
"""
import json, os, re, subprocess, sys

CONF = os.path.expanduser('~/.config/anon-scrub/terms.json')
ROOT = subprocess.run(['git', 'rev-parse', '--show-toplevel'], capture_output=True, text=True).stdout.strip() or os.getcwd()
TEXT = ('.md', '.csv', '.tsv', '.json', '.txt', '.html', '.py', '.yml', '.yaml', '.js', '.cjs', '.mjs', '.gitignore')


def load():
    if not os.path.exists(CONF):
        sys.exit(f'anonymize: {CONF} is missing, refusing to continue')
    c = json.load(open(CONF))
    return [(re.compile(p), r) for p, r in c['replace']], [(re.compile(p), r) for p, r in c['paths']]


def files():
    out = subprocess.run(['git', 'ls-files', '-co', '--exclude-standard'], cwd=ROOT, capture_output=True, text=True).stdout.split('\n')
    return [f for f in out if f and os.path.isfile(os.path.join(ROOT, f))]


def sentence_case(text, start):
    """True if the match starts a sentence, a line or a table cell."""
    before = text[max(0, start - 3):start]
    return start == 0 or before.endswith(('\n', '. ', '! ', '? ', '| ', '# ', '- ', '* ', '**')) or before.rstrip().endswith(('\n', '|'))


def scrub(text, rules):
    for pat, rep in rules:
        def sub(m, rep=rep):
            r = rep
            if r[:1].islower() and sentence_case(m.string, m.start()):
                r = r[0].upper() + r[1:]
            return r
        text = pat.sub(sub, text)
    return text


def main():
    rules, paths = load()
    mode = sys.argv[1] if len(sys.argv) > 1 else '--check'
    if mode == '--check-msg':
        msg = open(sys.argv[2]).read()
        hits = [p.pattern for p, _ in rules if p.search(msg)]
        if hits:
            sys.exit('anonymize: the commit message contains an identifying term; reword it')
        return
    bad = []
    for f in files():
        full = os.path.join(ROOT, f)
        new_rel = f
        for p, r in paths:
            new_rel = p.sub(r, new_rel)
        if f.endswith(TEXT) or os.path.basename(f) == '.gitignore':
            t = open(full, encoding='utf-8', errors='surrogateescape').read()
            n = scrub(t, rules)
            if n != t:
                if mode == '--fix':
                    open(full, 'w', encoding='utf-8', errors='surrogateescape').write(n)
                else:
                    bad.append(f)
        if new_rel != f:
            if mode == '--fix':
                os.makedirs(os.path.dirname(os.path.join(ROOT, new_rel)) or ROOT, exist_ok=True)
                os.rename(full, os.path.join(ROOT, new_rel))
            else:
                bad.append(f + ' (file name)')
    if mode == '--check' and bad:
        print('anonymize: identifying terms left in:\n  ' + '\n  '.join(sorted(set(bad))))
        print('run: python3 tools/anonymize.py --fix')
        sys.exit(1)
    if mode == '--fix':
        print('anonymize: done')


if __name__ == '__main__':
    main()
