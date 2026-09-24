+++
id = "lem-a1-middle-extension-dual-triangle"
kind = "lemma"
title = "The dual localization triangle for a curve middle extension"
order = 4295
uses = ["def-weil-open-closed-recollement", "def-weil-ordinary-compact-cohomology", "def-wf-middle-extension", "def-wf-tate-twist", "fix-cor-verdier-exchange", "lem-a1-finite-boundary-cohomology", "thm-pur-rational-and-qbar-purity"]
+++
Let $\bar C_0$ be a smooth projective curve, let
$j:U_0\hookrightarrow\bar C_0$ be dense open with finite closed
complement $i:Z_0\hookrightarrow\bar C_0$, and let $\mathcal F$
be lisse on $U_0$. Put $M=j_*\mathcal F$, using the ordinary
middle extension,
$B=i^*M$, and $\mathcal G=\mathcal F^\vee(1)$, with the
Tate twist. There is a canonical triangle

$$
i_*\mathbb D_Z B\longrightarrow\mathbb D_{\bar C}M
\longrightarrow Rj_*\mathcal G[2]\longrightarrow\ .
$$

In the cohomology
conventions of the blueprint, for every $r\geq2$ it gives

$$
H^{-r}(\bar C,\mathbb D_{\bar C}M)
\cong H^{2-r}(U,\mathcal G),
$$

and in the two remaining degrees it gives the exact sequence

$$
\begin{aligned}
0\longrightarrow H^{-1}(\bar C,\mathbb D_{\bar C}M)
&\longrightarrow H^1(U,\mathcal G)
\longrightarrow H^0(Z,\mathbb D_ZB)\\
&\longrightarrow H^0(\bar C,\mathbb D_{\bar C}M)
\longrightarrow H^2(U,\mathcal G)\longrightarrow0.
\end{aligned}
$$

The third term of the triangle is the derived direct image;
its positive direct-image sheaves cannot be discarded.

## Proof

Smooth purity [thm-pur-rational-and-qbar-purity] in dimension
one identifies $\mathbb D_U\mathcal F$ with
$\mathcal F^\vee(1)[2]=\mathcal G[2]$.
Apply the contravariant exact functor $\mathbb D_{\bar C}$ to
the triangle

$$
j_!\mathcal F\longrightarrow M\longrightarrow i_*B
\longrightarrow
$$

of [def-weil-open-closed-recollement].
The formal exchange [fix-cor-verdier-exchange] identifies the
duals of its outside terms with $Rj_*\mathcal G[2]$ and
$i_*\mathbb D_ZB$, respectively, giving the asserted triangle.
At a geometric point of $Z$, duality over the field $\Qlb$ is
ordinary finite-dimensional duality, so $\mathbb D_ZB$ is a sheaf
in degree zero. The finite-boundary calculation
[lem-a1-finite-boundary-cohomology] therefore concentrates
$R\Gamma(Z,\mathbb D_ZB)$ in degree zero.
Use $R\Gamma(\bar C,Rj_*\mathcal G)=R\Gamma(U,\mathcal G)$
and take the long exact cohomology sequence. In degrees at most
$-2$ both adjacent boundary groups vanish. In degrees $-1,0$
one obtains exactly the displayed five nonzero terms; the map
$H^1(U,\mathcal G)\to H^0(Z,\mathbb D_ZB)$ need not vanish.
