+++
id = "lem-sc-brauer-injectivity"
kind = "lemma"
title = "Brauer classes are determined by the generic fibre"
order = 2248
uses = ["lem-sc-divisor-exact-sequence", "lem-sc-point-z-cohomology"]
+++
Let $X$ be a smooth proper scheme over a field $k$. The
restriction to the generic point induces an injection

$$
H^2(X_{\Et},\mathbf G_m)\longrightarrow
H^2(k(X)_{\Et},\mathbf G_m)=\operatorname{Br}(k(X)).
$$

## Proof

Let $j:\eta:=\operatorname{Spec}k(X)\to X$ be the generic point.
Since $X$ is smooth, every local ring $\mathcal O_{X,x}$ is
regular, and the divisor exact sequence (the stalk computation is
identical to that of [lem-sc-divisor-exact-sequence], with the
regular local rings $\mathcal O_{X,x}$ in place of
$\mathcal O_{\overline C,P}$; at points of codimension at least
two the quotient is trivial because the strict henselization of a
regular local ring of dimension at least two is a factorial ring, so
the cokernel is supported exactly at the codimension-one points)

$$
0\longrightarrow\mathbf G_m\longrightarrow j_*\mathbf G_m
\longrightarrow\bigoplus_{x\in X^{(1)}}i_{x*}\mathbf Z\longrightarrow0,
$$

the sum over the codimension-one points $x$ of $X$ with
$i_x:\{x\}\to X$, is exact. Its long exact sequence, together
with $H^q(X,j_*\mathbf G_m)=H^q(\eta,\mathbf G_m)$
($\Gamma(X,j_*-)=\Gamma(\eta,-)$ and $j_*$ is exact), gives

$$
\cdots\to H^1(X,\textstyle\bigoplus_xi_{x*}\mathbf Z)
\to H^2(X,\mathbf G_m)
\to H^2(\eta,\mathbf G_m)
\to H^2(X,\textstyle\bigoplus_xi_{x*}\mathbf Z)\to\cdots.
$$

Now $H^q(X,i_{x*}\mathbf Z)=H^q(\operatorname{Spec}k(x),\mathbf Z)$
(for a closed immersion $i$, $i_*$ is exact and
$i^*i_*=\mathrm{id}$). For the field $K:=k(x)$: $H^1$ vanishes
($\operatorname{Hom}(\operatorname{Gal},\mathbf Z)=0$, since
$\mathbf Z$ is torsion-free: cf. [lem-sc-point-z-cohomology]), and
$H^2(\operatorname{Spec}K,\mathbf Z)\cong H^1(\operatorname{Spec}K,\mathbf Q/\mathbf Z)$
(from the sequence $0\to\mathbf Z\to\mathbf Q\to\mathbf Q/\mathbf Z\to0$ and the vanishing of $H^q(\operatorname{Gal},\mathbf Q)$
for $q\geq1$, $\mathbf Q$ being uniquely divisible:
*reference: Stacks Project, Etale Cohomology: etale cohomology
of a field is Galois cohomology*). Therefore the long
exact sequence reads

$$
0\longrightarrow H^2(X_{\Et},\mathbf G_m)\longrightarrow
H^2(k(X)_{\Et},\mathbf G_m)\longrightarrow
\bigoplus_{x\in X^{(1)}}H^1(k(x),\mathbf Q/\mathbf Z),
$$

and in particular the restriction map is injective. (This is the
classical residue sequence of Grothendieck: *reference:
Grothendieck, Le groupe de Brauer III (Dix Exposés); Milne, Etale
Cohomology, III.4; Gille–Szamuely, Central Simple Algebras and
Galois Cohomology, Ch. 6*. Its Stacks Project form is the exact
sequence of sheaves of Theorem 59.68.1,
[Tag 03RI](https://stacks.math.columbia.edu/tag/03RI),
$0\to\mathbf G_{m,X}\to j_*\mathbf G_{m,\eta}\to \bigoplus_{x\in X_0}(i_x)_*\mathbf Z\to0$, with the vanishing of the
higher cohomology of the skyscraper quotient in Lemma 59.68.4,
[Tag 03RL](https://stacks.math.columbia.edu/tag/03RL); the
identification $\operatorname{Br}(K)\cong H^2_{\Et}( \operatorname{Spec}K,\mathbf G_m)$ for a field, used to read the
target as a Brauer group, is Theorem 59.61.6,
[Tag 03R7](https://stacks.math.columbia.edu/tag/03R7).)
