+++
id = "prose-02-44"
kind = "hidden"
title = "Unbounded complexes (1)"
order = 156
+++
Proper base change needs the comparison with the étale site only for
bounded-below complexes. Brown representability, however, takes place in the
unbounded derived category, so we extend the comparison to unbounded
complexes. The difficulty is that a morphism from a sheaf into an unbounded
complex $K$ involves in principle all the cohomology sheaves of $K$ at once,
and so does a cohomology sheaf of $Rg_*K$. Both depend on only finitely many
of them if Ext groups and cohomology of sheaves vanish above a fixed degree,
uniformly in the sheaf. The smallest such degree is the cohomological
dimension defined below.

Without such a bound, $\Hom$ out of the constant sheaf need not commute with
direct sums. For example, take
$\ell=2$ and $S=\operatorname{Spec}\mathbf R$. Here étale cohomology is
the cohomology of $\operatorname{Gal}(\mathbf C/\mathbf R)=\mathbf Z/2$, and
$H^q(\mathbf Z/2,\mathbf F_2)=\mathbf F_2$ for every $q\geq0$. Thus
$\operatorname{cd}_2(S)=\infty$, and $\Hom(\mathbf F_2,-)$ does not commute
with the direct sum $\bigoplus_{n\geq0}\mathbf F_2[n]$ (see the opening of
Section [chap-Construction-of-f]).

Over a field of finite cohomological dimension, the étale cohomology of
schemes of finite type is uniformly bounded. In that case every computation
in a fixed degree can be carried out on a bounded-below truncation. We use
the bounds in this way in
Proposition [proposition-unbounded-comparison-finite-coefficients] below and, later, in the proofs of
compactness and of the preservation of direct sums by $Rp_*$
(Lemmas [lemma-uniform-ext-bound]
and [lemma-uniform-bound-proper-direct-image]).
