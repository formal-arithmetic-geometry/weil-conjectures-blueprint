+++
id = "dag-lem-route-sfb-completed-coefficients"
kind = "dag-lemma"
title = "The three completed-coefficient comparisons, their inverse-image compatibility, and specialization to `ℤ_ℓ` and `ℚ_ℓ`."
name_showing = false
order = 178506
tags = ["sheaf-dag"]
split_from = "lemma-comparison-completed-coefficients--4"
dag_id = "lem-route-sfb-completed-coefficients"
dag_kind = "statement"
dag_status = "split"
serial = false
dag_lean = ["AlgebraicGeometry.ProEtale.sfb_completed_coefficients"]
uses = ["dag-sk-def-sfb-pullback-from-point-comp", "dag-def-weil-pbc-constant-sheaf"]
+++
Fix a prime $\ell$ and an algebraic closure $\overline{\mathbf Q}_\ell$ of $\mathbf Q_\ell$. A finite subextension means $\mathbf Q_\ell\subseteq E\subseteq\overline{\mathbf Q}_\ell$ of finite degree. Give $E$ its extending absolute-value topology, and put $\mathcal O_E=\{x\in E:|x|\le1\}$ `sk-def-sfb-condensed-ring`. A uniformizer $\pi\in\mathcal O_E$ means $(\pi)=\mathfrak m_{\mathcal O_E}$. The rings $\mathbf Z_\ell,\mathbf Q_\ell$ are as in `def-weil-l-adic-numbers`. All index categories are small in a universe containing these fields.

For a topological ring $T$, write $\underline T(S)=C(S,T)$ on profinite sets with the coherent topology, with pointwise operations `sk-def-sfb-condensed-ring`. Write $T_X=p_X^*\underline T$ for its coefficient ring object on the small pro-etale site of any scheme $X$ [sk-def-sfb-pullback-from-point, sk-def-sfb-pulled-back-coefficients]. For a ring $A$, write $A_*$ and $A_X$ for the constant ring sheaves on the point and on $X$, respectively. Use the tensor product of abelian sheaves over $\mathbf Z$, so ring objects mean unital associative rings, without a commutativity requirement [sk-def-sfb-ring-object, sk-def-sfb-sheaf-tensor]. Let $\alpha_{f,T}:f^*T_Y\xrightarrow{\sim}T_X$ be the monoidal composition isomorphism for $f:X\to Y$ [dag-sk-def-sfb-pullback-from-point-comp].

For each pair $(R,K,I)=(\mathcal O_E,E,(\pi))$ as above, and also for $(R,K,I)=(\mathbf Z_\ell,\mathbf Q_\ell,(\ell))$, let $i_X:R_X\to K_X$ be $p_X^*$ of the continuous inclusion. The following normalized comparison holds, simultaneously for all schemes and their morphisms.

There is a cone of ring homomorphisms $\rho_n:\underline R\to(R/I^n)_*$ for $n\ge0$, with the usual quotient reduction transitions, whose restriction to constant sections is exactly $x\mapsto[x]$. Its image under $p_X^*$ is a limit cone of ring objects for every $X$, and there is an isomorphism of diagrams
$$p_X^*((R/I^n)_*)\cong(R/I^n)_X.$$
For every $f:X\to Y$, applying $f^*$ to this cone over $Y$ gives a limit cone as well.

There are $R_X$-linear maps $\iota_{X,m}:R_X\to K_X$ for $m\ge0$ (where $K_X$ is restricted along $i_X$) with $\iota_{X,0}=i_X$ and $\iota_{X,m+1}\circ\ell=\iota_{X,m}$. They make $K_X$ the colimit, in sheaves of $R_X$-module objects `sk-def-sfb-module-objects`, of the sequence of regular modules with transition multiplication by $\ell$. Multiplication by $\ell$ on $K_X$ is invertible, and
$$\alpha_{f,K}\circ f^*(\iota_{Y,m})=\iota_{X,m}\circ\alpha_{f,R}.$$
For every ring object $B$ of abelian sheaves on $X$ on which multiplication by $\ell$ is invertible and every ring morphism $a:R_X\to B$, there is a unique ring morphism $b:K_X\to B$ with $b\circ i_X=a$.

With quotient rings as in `def-weil-pbc-algebra-hom-quotient`, there is an isomorphism of ring-valued quotient towers
$$e:(\mathbf Z_\ell/(\ell)^n)_{n\ge0}\xrightarrow{\sim}(\mathbf Z/\ell^n\mathbf Z)_{n\ge0},\qquad e_n([x])=\operatorname{PadicInt.toZModPow}(n)(x).$$
The transitions on both sides are the usual reductions.

Finally, let $A=\underline{\overline{\mathbf Q}_\ell}$ denote the finite-subextension-valued condensed ring `sk-def-sfb-qlbar-condensed`, and let $c$ be the ring-object cocone $\underline E\to A$ with inclusion legs, indexed by finite subextensions ordered by inclusion. The cocones $p_X^*c$ and $f^*p_Y^*c$ are colimits in ring objects for every $X,Y,f:X\to Y$. If $j_{Z,E}:E_Z\to p_Z^*A$ is the inclusion leg, their compatibility is the equality
$$\alpha_{f,A}\circ f^*(j_{Y,E})=j_{X,E}\circ\alpha_{f,E}.$$
No invertibility condition on $\ell$ on a scheme is assumed. Exponent zero in each quotient tower is the terminal zero ring.

(SHEAF DAG node `lem-route-sfb-completed-coefficients`; machine-alignment layer.) Split from [lemma-comparison-completed-coefficients--4]. DAG kind: statement. DAG status: split. Statement dependencies not drawn: `sk-def-sfb-condensed-ring`, `def-weil-l-adic-numbers`, `sk-def-sfb-pullback-from-point`, `sk-def-sfb-pulled-back-coefficients`, `sk-def-sfb-ring-object`, `sk-def-sfb-sheaf-tensor`, `sk-def-sfb-qlbar-condensed`, `sk-def-sfb-module-objects`, `def-weil-pbc-algebra-hom-quotient`, `def-pe-completed-coefficient-comparison-data`.
