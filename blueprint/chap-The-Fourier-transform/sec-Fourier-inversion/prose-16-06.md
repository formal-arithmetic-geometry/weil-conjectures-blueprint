+++
id = "prose-16-06"
kind = "hidden"
title = "Fourier inversion (1)"
order = 1228
+++
We integrate with compact supports, $Rp_{2!}$ rather than $Rp_{2*}$,
for two reasons. First, proper base change computes the stalks
of $Rp_{2!}$ as compactly supported cohomology of the fibres, and this
puts $H^1_c(\mathbf A^1,j_*M)$ at the origin. Second, the trace formula
holds for $Rp_{2!}$, so that on trace functions the transform becomes the
discrete Fourier transform (16.3) (proved in
Section [sec-The-Plancherel-formula]).

The shift $[r]$ is the one for which the transform preserves the
perverse heart. For example, on the line we will find
$\operatorname{FT}_\psi(E[1])=\delta_0(-1)$, whereas without the shift the
perverse sheaf $E[1]$ would go to $\delta_0(-1)[-1]$, which is not
perverse.

We work with a vector bundle $V\to S$ rather than the line alone,
because the proofs move along the base. For instance, the stalk formula is base change
to a point of the dual bundle, and Fourier inversion is a computation on
$V\times_SV^\vee\times_SV$, which reduces, fibre by fibre, to
Lemma [lemma-integral-linear-character] on $\mathbf A^r$. We prove
these two properties in
Propositions [proposition-base-change-fourier-inversion]
and [proposition-fourier-inversion], while the preservation of the heart is
Proposition [proposition-fourier-transform-perverse-heart].

Let $S$ be a scheme of finite type over $k_0$ or over $k$, let $V\to S$ be a vector
bundle of rank $r$, and let $V^\vee$ be its dual bundle. Write
$p_1,p_2$ for the projections of $V\times_SV^\vee$, and set

$$
\mathcal K_\psi=\langle\ ,\ \rangle^*\mathcal L_\psi,
\qquad
\operatorname{FT}_\psi(K)
=Rp_{2!}(p_1^*K\otimes\mathcal K_\psi)[r].
\tag{16.1}
$$

The kernel $\mathcal K_\psi$ is lisse of rank one, and since the six
operations preserve constructibility, this defines a triangulated
functor $\operatorname{FT}_\psi:\Dbc(V,E)\to\Dbc(V^\vee,E)$, normalized
by the shift $[r]$.
