+++
id = "lem-fd-realified-kernel-concentration"
kind = "lemma"
title = "Single-degree concentration of the realified kernel"
order = 2975
uses = ["def-fd-nonexceptional", "def-fd-transform", "def-weil-pbc-constructible-complexes", "def-weil-punctual-weights", "def-wf-fundamental-representation", "def-wf-middle-extension", "lem-fd-nonexceptional-dual", "lem-fd-realified-kernel-real", "lem-fd-transform-concentration", "prop-functor-package"]
+++
Let $j:U_0\hookrightarrow\mathbf A^1_{k_0}$ and $\mathcal M$ be as in
[lem-fd-realified-kernel-real] — that is, $j$ is a dense open
immersion with $U_0=\mathbf A^1_{k_0}\setminus S_0$ and $\mathcal M$ is an
irreducible lisse Weil
sheaf on $U_0$, unramified at infinity,
punctually $\iota$-pure of weight
$w$, with irreducible geometric fundamental representation of
[def-wf-fundamental-representation] and
middle extension that is
Fourier-nonexceptional — and let
$\mathcal K$, with
$\mathcal M^\dagger=\mathcal M^\vee\otimes\mathcal B_b$ and
$\iota(b)=q^w$, be the realified kernel of
[lem-fd-realified-kernel-real]. Then

$$
R^\nu p_{2,!}\mathcal K=0\qquad(\nu\neq1),
$$

and the Fourier–Deligne transform
$\operatorname{FT}_\psi(j_!\mathcal M)$ is a direct summand of the
degree-zero cohomology sheaf of $p_{2,!}\mathcal K[1]$, namely
$R^{1}p_{2,!}\mathcal K$.

## Proof

By
[lem-fd-transform-concentration] the transform of $j_!\mathcal M$
is concentrated in degree $0$, so
$p_{2,!}\bigl(p_1^*(j_!\mathcal M)\otimes^L\mathcal K_\psi\bigr)$ is
concentrated in degree $1$; by [lem-fd-nonexceptional-dual] the
same result applies to the input $\mathcal M^\dagger$, whose hypothesis
package is unchanged, giving the same vanishing for the second summand.
The compact-support direct image is an exact triangulated functor by
[prop-functor-package], hence additive, so it commutes with the
direct sum and $R^\nu p_{2,!}\mathcal K=0$ for $\nu\neq1$. Since
$\operatorname{FT}_\psi(j_!\mathcal M) =p_{2,!}\bigl(p_1^*(j_!\mathcal M)\otimes^L\mathcal K_\psi\bigr)[1]$ by
[def-fd-transform], and $p_{2,!}\mathcal K$ is the direct sum of the
two pushed-forward summands, $\operatorname{FT}_\psi(j_!\mathcal M)$ is
a direct summand of the degree-zero cohomology sheaf of
$p_{2,!}\mathcal K[1]$, namely $R^{1}p_{2,!}\mathcal K$.
