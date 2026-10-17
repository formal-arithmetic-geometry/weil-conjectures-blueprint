+++
id = "p-real-integral"
kind = "theorem"
title = "Integral models"
order = 2940
uses = ["cor-galois-lisse-representations", "def-wf-fundamental-representation", "lem-wf-weil-fundamental-representation", "lem-wf-weil-group-exact-sequence", "prop-wf-weil-sheaf-representation-equivalence", "sk-prop-sfb-qlbar-colimit-x", "thm-lisse-qlbar-representations"]
tags = ["latex:proposition"]
+++
Keep the notation of [prop-wf-weil-sheaf-representation-equivalence], and let $U_0\subseteq C_0$ be a
nonempty open subscheme with base change $U$ and geometric fundamental group
$\pi_1(U)$, the kernel of the degree map of $W(U_0)$ by
[lem-wf-weil-group-exact-sequence]. An $\mathcal O_E$-lattice in $V$ means a free
$\mathcal O_E$-submodule of rank $\dim_{E}V$ that spans $V$ over $E$.

Let $(V,\rho)$ be a lisse Weil sheaf on $U_0$, with $\rho$ its Weil
fundamental representation of [def-wf-fundamental-representation]. After replacing $E$ by a
finite extension there is an $\mathcal O_E$-lattice $L\subset V$ with

$$
\rho(\pi_1(U))L=L,\qquad L\otimes_{\mathcal O_E}E=V,
$$

and the image of $\pi_1(U)$ in $\operatorname{Aut}(L/\mathfrak m_E^nL)$ is
finite for every $n$. Such an $L$ is the geometric stalk of a lisse
$\cO_{E,U}$-module $\mathcal L$ on $U_{\mathrm{proét}}$, locally isomorphic to
$\cO_{E,U}^{\oplus\operatorname{rk}L}$, whose reductions $\mathcal L/\mathfrak m_E^n\mathcal L$
are the finite locally constant sheaves with stalk $L/\mathfrak m_E^nL$, and with
$\mathcal L\otimes_{\cO_{E,U}}\overline{\mathbf Q}_{\ell,U}$ the lisse
$\overline{\mathbf Q}_{\ell,U}$-module underlying $V|_{U}$.
