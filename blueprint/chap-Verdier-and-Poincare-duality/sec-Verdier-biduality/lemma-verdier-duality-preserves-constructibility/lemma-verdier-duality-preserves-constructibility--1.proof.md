+++
kind = "proof"
of = "lemma-verdier-duality-preserves-constructibility--1"
order = 835002
uses = ["lemma-flat-models-generators", "proposition-comparison-immersions", "lemma-internal-adjunction-two-exchange-formulas", "theorem-smooth-purity-all-admissible-coefficients", "proposition-six-operations-dctf--1", "proposition-six-operations-dctf--2", "proposition-six-operations-dctf--14", "proposition-composition-base-change-rf-shriek", "proposition-forgetting-supports-composition"]
+++
First replace $X$ by its reduction $r:X_{\mathrm{red}}\hookrightarrow X$.
The localization triangle for the empty open gives
$K\simeq Rr_*r^*K=Rr_!r^*K$. Pullback preserves bounded constructibility
and the Tor interval $[a,b]$. It therefore suffices to treat
$\mathbb D_X(R\iota_!Q)$ for a reduced closed subscheme
$\iota:Z\hookrightarrow X$, with $Q$ bounded constructible of Tor
amplitude in $[a,b]$.

Argue by Noetherian induction on the closed support $Z$. The empty case
is immediate. The bounded flat models of [lemma-flat-models-generators]
give a dense open on which $Q$ has a dual in $\Dctf$; in Lean this is
`AlgebraicGeometry.Etale.exists_dense_open_exactPairing`.
Since $k$ is perfect and $Z$ is reduced, its smooth locus is dense.
Choose a nonempty irreducible smooth open $W\subseteq Z$ inside the
perfect locus, of dimension $r\leq d$. Write $s:W\hookrightarrow X$ and
$P=Q|_W$.

Internal adjunction [lemma-internal-adjunction-two-exchange-formulas]
gives

$$
\mathbb D_X(Rs_!P)\simeq Rs_*\mathbb D_WP.
$$

The finite-coefficient smooth duality underlying
[theorem-smooth-purity-all-admissible-coefficients] gives
$\omega_W\simeq L[2r]$, where $L$ is a locally constant rank-one
$\Lambda$-sheaf. Here Lean uses
`AlgebraicGeometry.Etale.exists_dualizingComplex_iso_and_tensor`.
If $P^\vee$ is the dual of $P$, then
$\mathbb D_WP\simeq P^\vee\otimes^{\mathbf L}L[2r]$ is bounded
constructible of Tor amplitude in $[-b-2r,-a-2r]$.
The direct-image preservation in [proposition-six-operations-dctf--2],
with the bound of `AlgebraicGeometry.Etale.torAmplitudeIn_rightDerivedLowerStar`,
shows that $Rs_*\mathbb D_WP$ is bounded constructible of Tor amplitude
in $[-b-2r,-a]\subseteq[-b-2d,-a]$.

For $j:W\hookrightarrow Z$ and its reduced closed complement
$i:Z'\hookrightarrow Z$, apply $R\iota_!$ and then
$\cHom_{\Lambda_X}(-,\omega_X)$ to the localization triangle
$j_!j^*Q\to Q\to Ri_*i^*Q\to$.
Composition of direct images with compact support identifies the open
term with $Rs_!P$, and properness identifies the closed term with
$R(\iota i)_!i^*Q$. The open term is handled above and the closed term
by induction. Exactness of internal Hom in its first variable and
closure under extensions preserve both constructibility and the fixed
Tor interval. This is
`AlgebraicGeometry.Etale.verdierDual_rightDerivedLowerShriek_of_isClosedImmersion`;
applying it to $r:X_{\mathrm{red}}\hookrightarrow X$ proves the claim.
