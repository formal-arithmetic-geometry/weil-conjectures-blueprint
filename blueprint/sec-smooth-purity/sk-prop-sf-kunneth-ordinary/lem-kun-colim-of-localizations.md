+++
id = "lem-kun-colim-of-localizations"
kind = "lemma"
title = "Colimit of localizations"
order = 3131
uses = ["def-pc-separably-closed", "lem-kun-algebra-union"]
+++
Let $B$ be an integral $K$-algebra which is a filtered union
$B=\bigcup_{i\in I}B_i$ of its finite type $K$-subalgebras, and
assume $L=\mathrm{Frac}(B)$ is a field (e.g. algebraically closed).
Let $J$ be the set of pairs $(i,g)$ with $i\in I$ and
$g\in B_i\setminus\{0\}$, ordered by $(i',g')\ge(i,g)$ if and only
if $B_i\subseteq B_{i'}$ and the image of $g$ in $(B_{i'})_{g'}$
is a unit. Then

$$
L=\varinjlim_{(i,g)\in J}(B_i)_g .
$$
