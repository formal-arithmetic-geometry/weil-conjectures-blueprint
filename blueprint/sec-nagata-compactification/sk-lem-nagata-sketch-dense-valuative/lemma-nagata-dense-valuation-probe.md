+++
id = "lemma-nagata-dense-valuation-probe"
kind = "lemma"
title = "Properties of the valuation probe"
order = 280
lean = ["AlgebraicGeometry.ValuativeCommSqWithPt.ofIsDominant"]
uses = ["def-nagata-dense-valuation-probe"]
+++
Let $h\colon T\to P$ be quasi-compact and dominant, and let $z\in P$. Then
$h$ has a valuation probe at $z$; in particular the maps in
$\mathsf{VP}(h,z)$ form a commutative diagram

$$
\begin{array}{ccc}
\operatorname{Spec}(K'_{h,z})&\xrightarrow{\eta_{h,z}}&T\\
\big\downarrow&&\big\downarrow h\\
\operatorname{Spec}(A'_{h,z})&\xrightarrow{\alpha_{h,z}}&P,
\end{array}
$$

and the closed point of $\operatorname{Spec}(A'_{h,z})$ maps to $z$.

## Proof

Since $h$ is dominant, $z$ lies in the closure of $h(T)$. Since $h$ is
quasi-compact, points in the closure of the image are specializations of
points of the image (Stacks Project, Lemma 29.6.5, Tag 02JQ): there is
$t\in T$ with $h(t)\rightsquigarrow z$. Consider the composite ring map

$$
\rho\colon\mathcal O_{P,z}\longrightarrow\mathcal O_{P,h(t)}
\longrightarrow\mathcal O_{T,t}\longrightarrow\kappa(t),
$$

the first map being the specialization map. Its kernel is a prime ideal
contained in $\mathfrak m_z$, so its image $B\subseteq\kappa(t)$ is a local
domain with maximal ideal $\rho(\mathfrak m_z)$. By Chevalley's theorem
(Stacks Project, Tag 00IA) there is a valuation ring $A'$ with fraction field
$K'=\kappa(t)$ that contains $B$ and dominates it. Let
$\eta\colon\operatorname{Spec}(\kappa(t))\to T$ be the canonical morphism,
and let $\alpha$ be the composite
$\operatorname{Spec}(A')\to\operatorname{Spec}(\mathcal O_{P,z})\to P$
induced by $\mathcal O_{P,z}\to B\subseteq A'$. Both composites
$\operatorname{Spec}(K')\to P$ in the square are induced by $\rho$, so the
square commutes. Since $A'$ dominates $B$, the maximal ideal of $A'$
contracts to $\mathfrak m_z$, so $\alpha$ maps the closed point of
$\operatorname{Spec}(A')$ to $z$. Thus $(A',K',\eta,\alpha)$ is a valuation
probe of $h$ at $z$ ([def-nagata-dense-valuation-probe]).
