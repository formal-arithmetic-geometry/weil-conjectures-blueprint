+++
kind  = "proof"
of    = "lem-pc-serre-vanishing"
+++
By the very-ample power condition in [def-sc-ample], choose
$m\ge1$ and a closed immersion $i:X\hookrightarrow\mathbf P^N_k$
with $i^*\mathcal O(1)=\mathcal L^{\otimes m}$.
For $0\le r<m$, put
$\mathcal G_r=i_*(\mathcal F\otimes\mathcal L^{\otimes r})$.
These are coherent, and
[lem-pc-closed-immersion-coherent-cohomology] gives

$$
H^q(X,\mathcal F\otimes\mathcal L^{\otimes(mt+r)})
=H^q(\mathbf P^N_k,\mathcal G_r(t)).
$$

Here the twist is [def-pc-projective-space-twist]; the tensor
identity follows from $i^*\mathcal O(t)=\mathcal L^{\otimes mt}$.
For each of the finitely many $r$,
[lem-pc-projective-space-serre-vanishing] supplies $t_r\ge0$
such that the right side vanishes for $t\ge t_r$ and $q>0$.
Put $T=\max_r t_r$ and $n_0=mT$. If $n\ge n_0$, division with
remainder writes $n=mt+r$ with $0\le r<m$ and $t\ge T$.
The displayed identity then gives the required vanishing.
