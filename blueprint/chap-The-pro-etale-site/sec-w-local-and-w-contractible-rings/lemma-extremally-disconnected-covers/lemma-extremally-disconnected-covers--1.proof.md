+++
kind = "proof"
of = "lemma-extremally-disconnected-covers--1"
order = 53005
uses = ["proposition-gleason-s-theorem"]
+++
Take $S$ to be the space of ultrafilters on the underlying set of $T$,
which realizes $\beta(T^{\delta})$. The extension of the identity
$T^{\delta}\to T$ is continuous and sends the principal ultrafilter
at $t$ to $t$. It is therefore surjective, or equivalently an
epimorphism of compact Hausdorff spaces.

To prove that $S$ is projective, let $f:S\to Y$ be continuous and
$g:X\to Y$ a continuous surjection of compact Hausdorff spaces.
Choose a set-theoretic section $s:Y\to X$ of $g$. The map
$t\mapsto s(f(t))$, with $t$ viewed as a principal ultrafilter,
extends to a continuous map $h:S\to X$. The maps $g\circ h$ and $f$
agree on the dense set of principal ultrafilters, so they agree on $S$.
Thus $S$ is projective. Proposition [proposition-gleason-s-theorem]
then shows that $S$ is extremally disconnected.
