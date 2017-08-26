# gc-version generators helper.
# Requires Python 2.6.
#
# This script reads its input, replaces %VARIABLES%, and saves output.
#  - genversion <version> <append-hg> <input> <output>
# Expanded variables:
#  - %GC_VERSION% to <version>-<revid>
#  - %GC_RC_VERSION% to <version> in format x.x.x.x
#  - %GC_RC_VERSION_INT% to <version> in format x,x,x,x
#  - %GC_HG_REV% to <revid>
#
# <revid> may be empty regardless of <append-hg>
# if Mercurial is not available, or we're not building from Mercurial repository.
import os, sys, subprocess

assert len(sys.argv) >= 5, 'Do not run directly, use build system instead.'

version, appendHg, input, output = sys.argv[1:5]

rch = sys.argv[5] if len(sys.argv) > 5 else None

variables = {
    'GC_VERSION': version,
    'GC_SIMPLE_VERSION': version,
}

if rch is not None:
    if not os.path.exists(rch):
        rch = os.path.join(os.path.dirname(input), rch)
    with open(rch, 'r') as fp:
        variables['GC_RCH_DEFINITIONS'] = '/* generate-version.py: inserting {0} */\n'.format(rch)
        variables['GC_RCH_DEFINITIONS'] += fp.read()
else:
    variables['GC_RCH_DEFINITIONS'] = ''

parts = (version + '.0.0').split('.')[:4]
variables['GC_RC_VERSION']     = '.'.join(parts)
variables['GC_RC_VERSION_INT'] = ','.join(parts)

revID = ''

if appendHg == 'yes':
    # try to run hg
    try:
        out = subprocess.Popen('hg id -r tip -ni', shell = True, stdout = subprocess.PIPE).communicate()[0]
        if out:
            rev, num = out.split()
            revID = 'r{0}:{1}'.format(num, rev)
    except OSError:
        pass

variables['GC_HG_REV'] = revID
if revID:
    variables['GC_VERSION'] += '-{0}'.format(revID)

with open(input, 'r') as fp:
    template = fp.read()

for key, value in variables.iteritems():
    template = template.replace('%{0}%'.format(key), value)

with open(output, 'w') as fp:
    #fp.write(
    #    '//\n/// THIS FILE IS AUTOMATICALLY GENERATED, EDIT {0} INSTEAD\n//\n\n'.format(
    #        os.path.basename(input)
    #    )
    #)
    fp.write(template)