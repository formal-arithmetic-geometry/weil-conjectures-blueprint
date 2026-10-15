+++
kind = "proof"
of = "det-pe-stonean-cover"
+++
*1.* $\widehat E\cap\widehat F=\widehat{E\cap F}$ and $\beta D\setminus\widehat E=
\widehat{D\setminus E}$ (an ultrafilter contains exactly one of $E$, $D\setminus E$), so the
$\widehat E$ form a basis of clopen sets. Two distinct ultrafilters are separated by some $E$
contained in one and not the other, giving disjoint basic opens $\widehat E$,
$\widehat{D\setminus E}$; so $\beta D$ is Hausdorff. For compactness, let
$\{\widehat{E_i}\}$ be a family of basic closed sets with the finite intersection
property; then the $E_i$ have the finite intersection property (as
$\widehat{E_{i_1}}\cap\dots\cap\widehat{E_{i_n}}=\widehat{E_{i_1}\cap\dots\cap E_{i_n}}$
is nonempty iff the intersection is nonempty), so they lie in an ultrafilter, which belongs
to all $\widehat{E_i}$. Density: a nonempty $\widehat E$ has $E\neq\emptyset$ and contains
the principal ultrafilter at any $d\in E$.

*2.* Let $O=\bigcup_i\widehat{E_i}$ be open and $E=\bigcup_iE_i$. Then $O\subset\widehat E$,
which is closed, so $\overline O\subset\widehat E$. Conversely let $\mathfrak p\in\widehat E$
and $\widehat F$ a basic neighbourhood of $\mathfrak p$. Then $E\cap F\in\mathfrak p$ is
nonempty; a point $d\in E_i\cap F$ gives a principal ultrafilter in $\widehat{E_i}\cap
\widehat F\subset O\cap\widehat F$. So $\overline O=\widehat E$ is open.

*3.* In a compact Hausdorff space every ultrafilter on the underlying set converges to
exactly one point (compactness gives a cluster point, which is a limit for an ultrafilter;
Hausdorff gives uniqueness). The principal ultrafilter at $t$ converges to $t$, so $\pi$
extends the identity and is surjective. Continuity: let $\pi(\mathfrak p)=t$ and $W\ni t$
open; choose an open $W'\ni t$ with $\overline{W'}\subset W$ (regularity). Then
$W'\in\mathfrak p$, and every $\mathfrak q\in\widehat{W'}$ contains $\overline{W'}$, so its
limit lies in the closed set $\overline{W'}\subset W$. Thus $\pi(\widehat{W'})\subset W$.
