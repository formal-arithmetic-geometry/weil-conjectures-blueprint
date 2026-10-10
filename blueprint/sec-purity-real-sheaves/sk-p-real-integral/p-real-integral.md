+++
id = "p-real-integral"
kind = "theorem"
title = "Integral models"
order = 2596
uses = ["def-wf-fundamental-representation", "lem-wf-weil-fundamental-representation", "lem-wf-weil-group-exact-sequence", "prop-wf-weil-sheaf-representation-equivalence"]
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
$\mathcal O_E$-sheaf on $U$.
