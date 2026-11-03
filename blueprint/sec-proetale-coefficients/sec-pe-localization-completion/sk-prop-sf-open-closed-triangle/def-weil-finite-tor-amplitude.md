+++
id = "def-weil-finite-tor-amplitude"
kind = "definition"
title = "Finite Tor amplitude"
order = 1209
lean = ["DerivedCategory.torAmplitudeIn", "DerivedCategory.finiteTorAmplitude", "AlgebraicGeometry.ProEtale.boundedConstructible", "AlgebraicGeometry.ProEtale.DerivedCategory.torAmplitudeIn", "AlgebraicGeometry.ProEtale.DerivedCategory.constructibleFiniteTor", "DerivedCategory.torAmplitudeIn.mono", "AlgebraicGeometry.ProEtale.DerivedCategory.torAmplitudeIn.mono", "AlgebraicGeometry.ProEtale.DerivedCategory.finiteTorAmplitude"]
uses = ["def-sfb-bounded-constructible-complexes", "def-weil-derived-cohomology-sheaves", "def-weil-derived-tensor", "def-weil-finite-torsion-constructibility", "det-def-sfb-bounded-constructible", "det-def-sfb-derived-tensor-hom"]
+++
Fix a prime $\ell$, a finite extension $E/\Ql$ with uniformizer $\pi_E$, an
integer $n\in\mathbf Z_{\geq1}$, and a scheme $Y$ on which $\ell$ is
invertible. Put $A_{E,n}=\mathcal O_E/\pi_E^n$, let
$\Lambda\in\{A_{E,n},\mathcal O_E,E,\Qlb\}$, regarded as a condensed ring with
coefficient sheaf $\Lambda_Y=p_Y^*\Lambda$, and use the derived cohomology
sheaves [def-weil-derived-cohomology-sheaves] and the derived tensor product
over $\Lambda_Y$ ([det-def-sfb-derived-tensor-hom]; [def-weil-derived-tensor]
for finite $\Lambda$). For integers $a\leq b$, an object
$K\in D(Y_{\mathrm{proét}},\Lambda)$ has *Tor amplitude in $[a,b]$* if, for
every sheaf $M$ of $\Lambda_Y$-modules placed in degree zero,

$$
 \mathcal H^r(K\otimes^L_{\Lambda_Y} M)=0
 \qquad\text{for every }r\in\mathbf Z\setminus[a,b],
$$

and it has *finite Tor amplitude* if it has Tor amplitude in some $[a,b]$.
These two conditions make sense, with the same wording, for any commutative
condensed ring $\Lambda$ and any scheme $Y$. Define $D^b_{ctf}(Y,\Lambda)$ as
the full subcategory of the bounded constructible category
$D^b_c(Y,\Lambda)$ [det-def-sfb-bounded-constructible] (for
$\Lambda=A_{E,n}$: complexes that are bounded with constructible cohomology
sheaves [def-sfb-bounded-constructible-complexes], with the finite-torsion
constructibility condition [def-weil-finite-torsion-constructibility]) on the
objects of finite Tor amplitude. The definition is the same for every
$\Lambda$.

**Well-definedness.** Tor amplitude in $[a,b]$ is invariant under
isomorphism, and it widens: Tor amplitude in $[a,b]$ implies Tor amplitude in
$[a',b']$ whenever $a'\le a$ and $b\le b'$. If $K$ has Tor amplitude in
$[a,b]$ then $K[1]$ has Tor amplitude in $[a-1,b-1]$. If
$K'\to K\to K''\to K'[1]$ is a distinguished triangle and $K',K''$ have Tor
amplitude in $[a,b]$, so does $K$; and a direct summand of a complex with Tor
amplitude in $[a,b]$ has Tor amplitude in $[a,b]$. Hence the complexes of
finite Tor amplitude form a thick subcategory of $D(Y_{\mathrm{proét}},\Lambda)$,
and $D^b_{ctf}(Y,\Lambda)$ is the intersection of this thick subcategory with
$D^b_c(Y,\Lambda)$; it is a full triangulated subcategory.

For $A_{E,n}$, finite Tor amplitude is an additional condition and does not
follow from bounded constructibility. For $\Lambda\in\{\mathcal O_E,E,\Qlb\}$ it is automatic,
$D^b_{ctf}(Y,\Lambda)=D^b_c(Y,\Lambda)$; this is proved later, see
[lem-integral-ctf-equals-bc].
