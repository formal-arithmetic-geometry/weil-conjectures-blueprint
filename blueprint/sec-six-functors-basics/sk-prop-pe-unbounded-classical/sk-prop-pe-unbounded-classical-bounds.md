+++
id = "det-pe-unbounded-classical-bounds"
kind = "lemma"
title = "Uniform cohomological bounds in the finite-type range"
order = 2132
uses = ["thm-sc-finite-type-torsion-cd", "lem-sc-cd-affine-limit", "det-base-field-cd-finite-field", "sk-prop-sf-comparison", "def-sc-etale-torsion-cd"]
+++
Let $k$ be a finite or algebraically closed field, $X$ and $Y$ schemes of finite
type over $k$, $g\colon X\to Y$ a morphism of finite type, and put
$e_X=2\dim X+1$, $e_Y=2\dim Y+1$. Let $G$ be a torsion sheaf on $X_{\Et}$.

1. If $U=\varprojlim_iU_i$ is a pro-étale affine presentation of an object of
   $X_{\Proet}$ ($U_i$ affine étale over $X$), then
   $H^q(U_{\Proet},(\nu_X^*G)|_U)=0$ for $q>e_X$.
2. If $V=\varprojlim_iV_i$ is a pro-étale affine presentation of an object of
   $Y_{\Proet}$ ($V_i$ affine étale over $Y$), then
   $H^q\bigl((X\times_YV)_{\Proet},(\nu_X^*G)|_{X\times_YV}\bigr)=0$ for
   $q>e_X$.
3. $R^qg_{\Et,*}G=0$ for $q>e_X$.

The same statements hold with $X$ replaced by $Y$ and $e_X$ by $e_Y$.
