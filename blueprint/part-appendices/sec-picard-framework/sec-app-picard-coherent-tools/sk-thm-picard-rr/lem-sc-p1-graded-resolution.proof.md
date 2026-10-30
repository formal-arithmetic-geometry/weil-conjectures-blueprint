+++
kind  = "proof"
of    = "lem-sc-p1-graded-resolution"
+++
By the description of coherent modules on $\operatorname{Proj}S$
(classical: the coherent module $\mathcal G$ is $\widetilde M$ for a
finitely generated graded module $M$ over $S=k[x_0,x_1]$), and the
graded Hilbert syzygy theorem (the polynomial ring $S$ has graded global
dimension two, so every finitely generated graded $S$-module has a graded
free resolution of length at most two), there is a graded free
resolution

$$
0\longrightarrow F_2\longrightarrow F_1\longrightarrow F_0
\longrightarrow M\longrightarrow0
$$

with the $F_i$ finite direct sums of graded free modules
$S(d)$; sheafifying (the functor $\widetilde{(-)}$ is exact) and
using $\widetilde{S(d)}=\mathcal O(d)$, the twisted structure
sheaf of [def-sc-p1-standard], which exists by
[lem-sc-p1-twist-exists], gives the displayed exact sequence
with $\mathcal E_i=\widetilde{F_i}$.
