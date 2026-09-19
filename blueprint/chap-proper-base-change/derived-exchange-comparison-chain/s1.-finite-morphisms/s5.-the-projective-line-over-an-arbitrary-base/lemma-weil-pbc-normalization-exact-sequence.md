+++
id = "lemma-weil-pbc-normalization-exact-sequence"
kind = "lemma"
title = "Normalization comparison exact sequence"
order = 740
uses = ["def-weil-pbc-finite-open-comparison", "lemma-weil-pbc-eight-curve-devissage", "lemma-weil-pbc-finite-pushforward-extension-zero"]
+++
Let $X$ be a reduced curve over an algebraically closed field,
$\nu:X^\nu\to X$ its finite normalization, $j:U\hookrightarrow X$ open,
and $j^\nu:U^\nu\hookrightarrow X^\nu$ its pullback. For every prime
$\ell$, the unit and the finite-open comparison define a monomorphism

$$
\alpha:j_!\underline{\mathbf F_\ell}\longrightarrow
\nu_*j^\nu_!\underline{\mathbf F_\ell}
$$

whose cokernel $Q$ is constructible and supported on the finite nonnormal
locus. The sequence

$$
0\longrightarrow j_!\underline{\mathbf F_\ell}
\xrightarrow{\alpha}\nu_*j^\nu_!\underline{\mathbf F_\ell}
\longrightarrow Q\longrightarrow0
$$

and all its cohomology boundary maps commute with algebraically closed field
extension and restriction to opens.

## Proof

Let $v:U^\nu\to U$. Define $\alpha$ as

$$
j_!\underline{\mathbf F_\ell}
\xrightarrow{j_!\eta}
j_!v_*\underline{\mathbf F_\ell}
\xrightarrow{\beta_{\nu,j}}
\nu_*j^\nu_!\underline{\mathbf F_\ell},
$$

where $\eta$ is the unit of $v^{-1}\dashv v_*$ and $\beta$ is the comparison
map already constructed. At $\bar x\in U$, its stalk is the diagonal

$$
\mathbf F_\ell\longrightarrow
\bigoplus_{\bar z\in\nu^{-1}(\bar x)}\mathbf F_\ell,\qquad
a\longmapsto(a)_{\bar z};
$$

outside $U$, both stalks are zero. Normalization is surjective, so the
diagonal is injective. Over the dense open where $\nu$ is an isomorphism it
is an isomorphism. Therefore the cokernel $Q$ is supported on the finite
nonnormal locus, with stalk the quotient of the displayed finite sum by its
diagonal. This proves exactness and constructibility.

After an algebraically closed extension, $X^\nu$ remains smooth and normal
and is the normalization of the reduced base-changed curve. The unit stalk
map remains the diagonal, while the base-change rectangle for $\beta$
identifies the two pulled-back comparison maps. Thus the short exact
sequence pulls back to the primed sequence. Naturality of the connecting
homomorphism follows by applying compatible injective resolutions. For an
open $W\subset X$, finite base change replaces $\nu$ by
$\nu^{-1}W\to W$ and gives the same stalk diagonals, proving compatibility
with open restriction.

Finally $H^q(X,Q)=0$ for $q>0$, and
$H^0(X,Q)$ is the finite direct sum of its stalks; both statements persist
after base change. Exact finite direct image and Leray identify
$H^q(X,\nu_*j^\nu_!\mathbf F_\ell)$ with
$H^q(X^\nu,j^\nu_!\mathbf F_\ell)$. Hence the displayed long exact
sequence transfers vanishing, finiteness, field-extension isomorphisms, and
open-restriction surjectivity from the normalized term to
$j_!\mathbf F_\ell$: in degrees at least two the maps are isomorphisms, and
in degrees zero and one the finite sequence

$$
0\to H^0(j_!\mathbf F_\ell)\to H^0(\nu_*j^\nu_!\mathbf F_\ell)
\to H^0(Q)\to H^1(j_!\mathbf F_\ell)\to
H^1(\nu_*j^\nu_!\mathbf F_\ell)\to0
$$

gives the comparison by a five-lemma diagram.
