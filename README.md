# xterm_color
Colorful/Colourful Xterms

I like xterms to have light text on a dark background. Since I usually have a lot of xterms open, I like them to have random colors for visual texture (the main requirement is that the background must be dark). This program is a wrapper for xterm that generates each new xterm with a different random color (random, but the overall hue of the xterm can be gamed).

## Installation

You will want to have xterm and python installed. This program assumes that xterm is installed at <code>/usr/bin/xterm</code> and python is installed at <code>/usr/bin/python</code>.

Create symbolic links from both 'xterm' and xterm_color.py to a place in your path that has higher priority than the location of your system xterm program. Alternatively, put this repository in your path.

## Usage

Call xterm: <code>$ xterm &</code>. You now have an xterm with a random background color.

Want your background hue to be weighted towards being bluish? Try: <code>$ xterm blue &</code>
Want another blue xterm, but with a different color than the last one? Just run the above command again.

Try the above replacing <code>blue</code> with <code>red</code>, <code>green</code>, or <code>grey</code>.

## Disclaimer

This software is tailored pretty closely to my own personal needs. If somebody feels that this program is useful, I could spend some time making it more robust.
