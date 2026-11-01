+++
id = "lem-fix-operation-reduction"
kind = "lemma"
title = "Basic operations and coefficient reduction"
order = 3521
uses = ["def-weil-derived-direct-image", "def-weil-derived-pullback-tensor-hom", "det-prop-scalar-six-exceptional", "def-weil-site-perfect-complex", "lem-fix-compact-support-coefficient-change", "lem-weil-pbc-standard-quotients-perfect", "lemma-weil-pbc-perfect-projection-formula", "def-pe-derived-complete", "sk-prop-integral-criterion", "det-def-sfb-coefficient-comparisons", "sk-prop-scalar-six", "det-prop-scalar-six-compact-support"]
+++
For the condensed integral categories $\Dbc(-,\mathcal O_E)$, whose objects
are derived $\pi_E$-complete $\mathcal O_{E,X}$-complexes
([def-pe-derived-complete], [sk-prop-integral-criterion]), reduction
$\mathcal O_E\to A_{E,n}$, $K\mapsto K_n=K\otimes^{\mathbf L}_{\mathcal O_{E,X}}(A_{E,n})_X$,
commutes with derived pullback, tensor, ordinary direct image and
compact-support direct image on their stated bounded domains. Finite
reduction $A_{E,n}\to A_{E,m}$ commutes with pullback, tensor and
compact-support direct image on the finite-Tor domains.
For $\mathcal O_E\to A_{E,n}$, internal Hom and evaluation commute
with reduction for arbitrary first variables on the stated integral
domains. Between finite quotient rings, the elementary comparison
proved here assumes that the first variable is
site-perfect; this includes
the coefficient dual of a perfect complex at a point.
For the exceptional inverse image, the comparison
$(Rf^!K)_{\Lambda'}\cong Rf^!(K_{\Lambda'})$ along every finite-ring map
$A\to B$, in particular $A_{E,n}\to A_{E,m}$, and along
$\mathcal O_E\to A_{E,n}$, is that of [det-prop-scalar-six-exceptional].
The same operations and comparisons commute with localization
$\mathcal O_E\to E$ and with extension of scalars $E\to F\to\Qlb$ on the
condensed categories ([det-def-sfb-coefficient-comparisons],
[sk-prop-scalar-six]). All the displayed comparisons preserve the tensor
associativity maps, evaluations, units and counits used to construct
the projection and exchange transformations.

*Formalisation status (the statement is unchanged).* One clause is not yet
formalised: in the pro-étale model, that reduction modulo $\mathfrak m_E$
(that is, $\mathcal O_E\to A_{E,n}$) carries the projection map
$\mathrm{PF}_{f,K,L}$ to the projection map of the reductions
$\mathrm{PF}_{f,K_n,L_n}$. The étale projection map and the pro-étale
compact-support exchange map are covered, but the pro-étale projection map
needs that the pro-étale pullback preserves flat objects for a general
coefficient ring, which is not yet available. The completed pro-étale
projection formula for the scalar extensions $\mathcal O_E\to\mathcal O_{E'}$
depends on this clause (or on a comparison of the pullback from the étale to
the pro-étale site with derived completion), and is formalised so far only for
pro-étale realizations $K=\nu^*K_0$, $L=\nu^*L_0$ of étale complexes and
under the additional hypothesis that both sides of the étale projection map
$Rf_!K_0\otimes^{\mathbf L}L_0\to Rf_!(K_0\otimes^{\mathbf L}Lf^*L_0)$ are derived
complete.
