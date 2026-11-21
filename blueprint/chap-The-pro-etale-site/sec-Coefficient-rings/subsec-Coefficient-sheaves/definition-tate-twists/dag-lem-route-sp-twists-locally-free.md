+++
id = "dag-lem-route-sp-twists-locally-free"
kind = "dag-lemma"
title = "The constructed integral, rational and sheafified-colimit lines are locally free of rank one over their respective pulled-back condensed coefficient r"
name_showing = false
order = 184531
tags = ["sheaf-dag"]
split_from = "definition-tate-twists--10"
dag_id = "lem-route-sp-twists-locally-free"
dag_kind = "statement"
dag_status = "split"
serial = false
dag_lean = ["AlgebraicGeometry.ProEtale.spTwists_locallyFree"]
uses = ["dag-def-weil-pbc-proetale-site"]
+++
Fix a prime $\ell$, an algebraic closure $\Omega=\overline{\mathbf Q}_\ell$ of $\mathbf Q_\ell$, a scheme $X$ such that $\ell$ is invertible in every residue field, and a finite intermediate field $\mathbf Q_\ell\subseteq E\subseteq\Omega$. Use the universe convention `def-weil-size-convention` and the small pro-etale site $C=X_{\mathrm{proet}}$ [dag-def-weil-pbc-proetale-site]. Use precisely the pulled-back condensed coefficient rings and constructed Tate lines of [dag-sk-def-sp-tate-twist]: $R_E=\mathcal O_{E,X}$, $K_E=E_X$, $A=\overline{\mathbf Q}_{\ell,X}$,
$$
 L_E=\varprojlim_{n\geq1}\left(\mu_{\ell^n,X}\otimes_{(\mathbf Z/\ell^n)_X}(\mathcal O_E/\ell^n)_X\right),\qquad
 Q_E=K_E\otimes_{R_E}L_E,\qquad
 Q_\Omega=\varinjlim_F Q_F.
$$
The integral limit has the coefficient-reduction and root-power transitions, and the last colimit is the sheafified colimit over the small directed poset of finite intermediate fields $F$ in $\Omega$, with its specified finite-extension transitions and $A$-action. In particular $A$ is the pullback of the finite-subextension-valued condensed coefficient ring. Read internal modules as sectionwise module sheaves through `def-weil-pbc-internal-abelian-sheaf-module-equivalence`, and let restriction to $C/U$ mean [dag-def-pur-localized-ringed-site].

Then $L_E$, $Q_E$ and $Q_\Omega$ are finite locally free of constant rank one over $R_E$, $K_E$ and $A$, respectively. Here rank one means that on a covering of the terminal object each restricted module has a basis indexed by a singleton, equivalently is linearly isomorphic to its restricted coefficient ring. This asserts the three rank-one clauses for the signed twists at exponent $1$ of the constructed lines, whose exponent $0$ is the coefficient unit. No quasi-compactness or finite-type hypothesis is imposed on $X$.

(SHEAF DAG node `lem-route-sp-twists-locally-free`; machine-alignment layer.) Split from [definition-tate-twists--10]. DAG kind: statement. DAG status: split. Statement dependencies not drawn: `def-weil-size-convention`, `sk-def-sp-tate-twist`, `def-weil-pbc-internal-abelian-sheaf-module-equivalence`, `def-pur-localized-ringed-site`.
