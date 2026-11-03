+++
id = "p-real-integral"
kind = "theorem"
title = "Integral models"
order = 3929
uses = ["cor-galois-lisse-representations", "sk-prop-sfb-qlbar-colimit-x", "thm-lisse-qlbar-representations"]
lean = ["AlgebraicGeometry.WeilGroup.IsLisse.exists_lattice"]
tags = ["latex:proposition"]
+++
Let $C_0$ be a smooth geometrically connected curve over $\Fq$, and let
$U_0\subseteq C_0$ be a nonempty open subscheme with base change $U$ and
geometric fundamental group $\pi_1(U)$. For a finite extension $E/\Ql$
inside $\overline{\mathbf Q}_\ell$, an $\mathcal O_E$-lattice in a
finite-dimensional $\overline{\mathbf Q}_\ell$-vector space $V$ means a free
$\mathcal O_E$-submodule of rank $\dim V$ whose
$\overline{\mathbf Q}_\ell$-span is $V$.

Let $\mathcal F$ be a lisse $\overline{\mathbf Q}_{\ell,U}$-module on
$U_{\mathrm{proét}}$ (for instance the sheaf underlying a lisse Weil sheaf
on $U_0$), and let $\rho:\pi_1(U)\to\operatorname{GL}(V)$ be its
geometric fundamental representation of
[thm-lisse-qlbar-representations]. After replacing $E$ by a
finite extension there is an $\mathcal O_E$-lattice $L\subset V$ with

$$
\rho(\pi_1(U))L=L,\qquad L\otimes_{\mathcal O_E}\overline{\mathbf Q}_\ell=V,
$$

and the image of $\pi_1(U)$ in $\operatorname{Aut}(L/\mathfrak m_E^nL)$ is
finite for every $n$. Such an $L$ is the geometric stalk of a lisse
$\cO_{E,U}$-module $\mathcal L$ on $U_{\mathrm{proét}}$, locally isomorphic to
$\cO_{E,U}^{\oplus\operatorname{rk}L}$, whose reductions $\mathcal L/\mathfrak m_E^n\mathcal L$
are the finite locally constant sheaves with stalk $L/\mathfrak m_E^nL$, and with
$\mathcal L\otimes_{\cO_{E,U}}\overline{\mathbf Q}_{\ell,U}\simeq\mathcal F$.
