+++
kind  = "proof"
of    = "sk-thm-picard-twist"
uses = ["sk-thm-picard-serre-b", "sk-thm-picard-rr", "sk-prop-picard-dense-points"]
+++
Choose an ample $\cM$ on $C$ ($C$ is projective). For $r\gg0$, Serre
vanishing ([sk-thm-picard-serre-b]) and Riemann–Roch
([sk-thm-picard-rr], valid on $C_K$ since $H^0(C_K,\cO_{C_K})=K$ by flat
base change) make $\cF=\cL\otimes\cM_K^{\otimes r}$ have zero $H^1$ and a
positive-dimensional space of sections:
$h^0(\cF)=\chi(\cF)=\deg\cL+r\deg\cM+1-g\to\infty$.

Whenever $h^0(\cF)$ is larger than $1$, choose a nonzero section $s$ and
a point $x\in C(k)$ where $s$ is nonzero. Such a point exists: $s$ has a
finite zero divisor on $C_K$, while $C(k)$ is infinite
([sk-prop-picard-dense-points]) and its distinct points remain distinct
on $C_K$. The sequence

$$
0\longrightarrow\cF(-x_K)\longrightarrow\cF\longrightarrow\cF|_{x_K}\longrightarrow0
$$

shows that subtraction of $x_K$ lowers $h^0$ by exactly $1$ and preserves
$H^1=0$: in the long exact sequence, $h^0(\cF|_{x_K})=1$, the map
$H^0(\cF)\to H^0(\cF|_{x_K})$ is onto because $s(x_K)\ne0$, and
$H^1(\cF(-x_K))\to H^1(\cF)=0$ is injective, its kernel being the
cokernel of that onto map. Continue until $h^0=1$. All subtracted points
come from $k$, so the resulting twist has the form
$\cM_0=\cM^{\otimes r}(-x_1-\cdots-x_s)$ on $C$, with
$\cM_{0,K}=\cM_K^{\otimes r}(-x_{1,K}-\cdots-x_{s,K})$. Normalization
along a rational point $P$ does not change the fibre cohomology
dimensions (it tensors with the pullback of a line bundle on the
base field, which is trivial). This is the twist argument of Stacks
Project, Tag 0B9Y.
