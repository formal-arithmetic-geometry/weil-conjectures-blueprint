+++
id = "prose-09-11"
kind = "hidden"
title = "Finite coefficients (1)"
order = 744
+++
Since $f^!K\simeq f^*K\otimes^{\mathbf L}\omega_f$, smooth purity with finite
coefficients comes down to a single global isomorphism
$\omega_f\simeq(\mathbf Z/\ell^n\mathbf Z)_X(d)[2d]$.
We obtain it from the diagonal $\Delta:X\to X\times_YX$, which is a section
of the smooth projection $p_1$. Deformation to the normal bundle moves
$\Delta$ to the zero section of the relative tangent bundle $T_{X/Y}$,
where Proposition [proposition-purity-vector-bundles] gives the
isomorphism.

We use the diagonal because it is attached to $f$ without choices, and
because $\omega_f$ is recovered from it: $\omega_f\simeq\Delta^*\omega_{p_1}$
by base change. Near the diagonal, however, $X\times_YX$ looks like a neighbourhood
of the zero section in $T_{X/Y}$ only to first order, and the deformation makes
this precise without choosing a tubular neighbourhood. The comparison it
yields, Lemma [lemma-section-normal-bundle], is determined by the
requirement that it be the identity at $t=1$.

The deformation argument works for any section of a smooth morphism. Let $g:V\to S$ be smooth of pure
relative dimension $d$ and let $s:S\to V$ be a section of $g$ that is a
closed immersion. Then $s$ is a regular immersion of codimension $d$, and
we let $N_s$ be its normal bundle, with projection $\pi:N_s\to S$ and zero
section $z:S\to N_s$.
