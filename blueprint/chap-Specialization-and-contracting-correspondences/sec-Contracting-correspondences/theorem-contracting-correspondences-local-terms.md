+++
id = "theorem-contracting-correspondences-local-terms"
kind = "theorem"
title = "Contracting correspondences and local terms"
order = 1700
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.Correspondence.restrict_traceClass_eq_pushforward_of_isContractingAt"]
+++
Let $c=(c_1,c_2):C\to X\times X$ be a correspondence, and let
$Z\hookrightarrow X$ have ideal $I$. Let $F_0$ be a connected component
of $\Fix(c)$ that is open and closed and whose image meets $Z$. Choose
an open neighbourhood $W\subset C$ of $F_0$ on which

$$
I_2=c_2^{-1}(I)\mathcal O_W\subset
I_1=c_1^{-1}(I)\mathcal O_W,
\qquad I_2^n\subset I_1^{n+1}\quad\text{for some }n\geq1.
$$

Let $K\in D^b_{\mathrm{ctf}}(X,A)$, let $u:c_2^*K\to c_1^!K$ be a cohomological
correspondence, and let $u_Z$ be the restriction
(E.22) to $Z$ of $u|_W$, for the
correspondence $c|_W$, with $c_Z:C_Z=(W\cap c_1^{-1}Z)_{\mathrm{red}}\to
Z_{\mathrm{red}}\times Z_{\mathrm{red}}$. Then $h_{F_0}$ is an
isomorphism after reduction, and

$$
\operatorname{Tr}_c(u)|_{F_0}
=(h_{F_0})_*\bigl(\operatorname{Tr}_{c_Z}(u_Z)|_{F_{0,Z}}\bigr),
$$

where $(h_{F_0})_*:H^0(F_{0,Z},\omega_{F_{0,Z}})\to H^0(F_0,\omega_{F_0})$
is the induced isomorphism. In particular, if $F_0$ is proper, then
$\operatorname{LT}_{F_0}(u)=\operatorname{LT}_{F_{0,Z}}(u_Z)$.
