+++
id = "sk-thm-tf-contracting-local-term"
kind = "theorem"
title = "Contracting correspondences and local terms"
order = 974
uses = ["sk-i-additivity", "sk-d-trace-class", "sk-lem-tf-contracting-fixed-geometry", "sk-cor-tf-sp-fixed-constant", "sk-thm-tf-sp-zero-section", "sk-lem-tf-contracting-cone-geometry", "sk-prop-tf-trace-specialization", "sk-p-proper"]
tags = ["sketch"]
+++
Let $c=(c_1,c_2):C\to X\times X$ be a correspondence, and let
$Z\hookrightarrow X$ have ideal $I$. Let $F_0$ be a connected component of $\Fix(c)$ that is open and closed and
whose image meets $Z$. Choose an open neighbourhood $W\subset C$
of $F_0$ on which

$$
I_2=c_2^{-1}(I)\mathcal O_W\subset
I_1=c_1^{-1}(I)\mathcal O_W,
\qquad I_2^n\subset I_1^{n+1}\quad\text{for some }n\geq1.
$$

As in Proposition [sk-i-additivity], let
$C_Z=(W\cap c_1^{-1}Z)_{\mathrm{red}}$, and let
$c_Z=(c_{Z,1},c_{Z,2}):C_Z\to Z_{\mathrm{red}}\times Z_{\mathrm{red}}$
be the correspondence induced by the two legs restricted to $W$.
Let $K\in D^b_{\mathrm{ctf}}(X,A)$, let $K_Z$ be its restriction to $Z_{\mathrm{red}}$,
and let $u:c_2^*K\to c_1^!K$ be a cohomological correspondence. Then the
cohomological correspondence $u_Z:c_{Z,2}^*K_Z\to c_{Z,1}^!K_Z$ constructed
in the proof satisfies

$$
\operatorname{Tr}_c(u)|_{F_0}
=(h_{F_0})_*\bigl(\operatorname{Tr}_{c_Z}(u_Z)|_{F_{0,Z}}\bigr),
\qquad F_{0,Z}=\Fix(c_Z)\times_{\Fix(c)}F_0.
$$

Here the projection $h_{F_0}:F_{0,Z}\to F_0$ is an isomorphism
after reduction, and $(h_{F_0})_*$ is the induced isomorphism
$H^0(F_{0,Z},\omega_{F_{0,Z}})\simeq H^0(F_0,\omega_{F_0})$. If $F_0$ is proper, the local terms of $u$ on $F_0$ and
of $u_Z$ on $F_{0,Z}$ are equal.
