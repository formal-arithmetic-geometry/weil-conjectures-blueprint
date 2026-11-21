+++
id = "dag-lem-route-sp-integral-twist-level-comparison"
kind = "dag-lemma"
title = "The finite-level twist is the displayed constant-ring scalar extension."
name_showing = false
order = 187544
tags = ["sheaf-dag"]
split_from = "lemma-inverse-image-coefficient-sheaves--2"
dag_id = "lem-route-sp-integral-twist-level-comparison"
dag_kind = "statement"
dag_status = "split"
serial = false
dag_lean = ["AlgebraicGeometry.ProEtale.spIntegralTwistLevel_comparison"]
uses = ["dag-def-weil-pbc-proetale-site", "dag-def-pur-roots-of-unity-sheaf", "dag-lem-sp-ell-quotient-finite-discrete"]
+++
Let $X$ be any scheme, let $\ell$ be prime, fix an algebraic closure $\overline{\mathbf Q}_\ell$, and let $E\subseteq\overline{\mathbf Q}_\ell$ be a finite intermediate extension. Write $O_E$ for its ring of integers with the topology restricted from the fixed algebraic closure [def-weil-l-adic-coefficient-extension, sk-def-sfb-condensed-ring]. Work on the small pro-etale site of $X$, small relative to abelian sheaves [def-weil-pbc-proetale-site, def-weil-size-convention]. For $n\geq0$, put $N=\ell^{n+1}$ and $B=O_E/(N)$, with the discrete topology. Write $\widetilde B=\operatorname{ULift}(B)$ for the universe lift used in constant coefficient sheaves. Let $C=p_X^*\underline B$ and $R=p_X^*\underline{O_E}$ be the pulled-back continuous-function ring objects `sk-def-sfb-pulled-back-coefficients`, with $\rho:R\to C$ induced by reduction. Let $M=\mu_{N,X}$ be the actual roots-of-unity abelian sheaf with its specified constant $(\mathbf Z/N)_X$-action [dag-def-pur-roots-of-unity-sheaf].

In the tensor category of abelian sheaves `det-def-sfb-sheaf-tensor-structure`, let $F_C(M)$ denote the internal $C$-module with underlying object $C\otimes_{\mathbf Z}M$ and action given by multiplication on the first factor `sk-def-sfb-module-objects`. The native integral level is $Q_{E,n}=\operatorname{Res}_{\rho}F_C(M)$, namely the construction `spIntegralTwistLevel X ℓ E n`. For a unital map $a:\mathbf Z/N\to\widetilde B$, let $L_a=\widetilde B_X\otimes_{(\mathbf Z/N)_X}M$ be the finite Tate line `def-pur-finite-tate-line-signed-comparison`, namely `Scheme.tateFiniteLine X ℓ (ULift B) n a`.

There exists a unital ring map $a:\mathbf Z/N\to\widetilde B$ and an isomorphism of abelian sheaves
$$U(Q_{E,n})\cong U(L_a),$$
where $U$ forgets the respective coefficient actions. No invertibility assumption on $\ell$ on $X$ is needed.

(SHEAF DAG node `lem-route-sp-integral-twist-level-comparison`; machine-alignment layer.) Split from [lemma-inverse-image-coefficient-sheaves--2]. DAG kind: statement. Placed through `det-prop-sfb-cartesian-coefficients-twists` (ancestor-1). DAG status: split. Statement dependencies not drawn: `def-weil-l-adic-coefficient-extension`, `sk-def-sfb-condensed-ring`, `def-weil-size-convention`, `sk-def-sfb-pulled-back-coefficients`, `det-def-sfb-sheaf-tensor-structure`, `sk-def-sfb-module-objects`, `def-pur-finite-tate-line-signed-comparison`.
