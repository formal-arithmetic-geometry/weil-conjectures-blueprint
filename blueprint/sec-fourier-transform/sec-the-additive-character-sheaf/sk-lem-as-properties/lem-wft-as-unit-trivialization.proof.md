+++
kind  = "proof"
of    = "lem-wft-as-unit-trivialization"
+++
Work with the $k_0$-model of [def-fd-artin-schreier-sheaf]: the stalk of
$\mathcal L_\psi$ at a geometric point over $x$ is the space of functions
$\varphi$ on the $k_0$-torsor $\{y:y^q-y=x\}$ with
$\varphi(y+c)=\psi(c)\varphi(y)$; over $x=0$ the root $y=0$ is defined over
$k_0$, and $\varepsilon(\varphi)=\varphi(0)$ is an isomorphism because an
isotypic function is determined by one value.

*Multiplicativity.* Over $\mathbf A^2$ with coordinates $(x_1,x_2)$, adding
roots, $(y_1,y_2)\mapsto y_1+y_2$, maps the product of the covers of $x_1$
and $x_2$ to the cover of $x_1+x_2$, equivariantly for the addition
$k_0\times k_0\to k_0$. As in Step 5 of [lem-fd-as-characters] (whose
argument applies verbatim to the $k_0$-covers), pullback along this map
carries $m^*\mathcal L_\psi=\mathcal L_{\psi,x_1+x_2}$ isomorphically onto the
rank-one subsheaf of
$\operatorname{pr}_1^*\mathcal L_\psi\otimes\operatorname{pr}_2^*\mathcal L_\psi$
on which $(c_1,c_2)$ acts by $\psi(c_1)\psi(c_2)$, which is the whole tensor
product; this is $\mu$. At the origin, $(0,0)\mapsto0$, so
$\mu(\varphi)(0,0)=\varphi(0)$, which is the compatibility with
$\varepsilon$. Associativity holds because $(y_1+y_2)+y_3=y_1+(y_2+y_3)$ as
maps of the triple product of covers, and the unit compatibility because
$0+y_2=y_2$ on $\{0\}\times\mathbf A^1$ with the root $y_1=0$.

*Duality.* The map $y\mapsto-y$ identifies the cover of $x$ with that of
$-x$ and intertwines $\sigma_c$ with $\sigma_{-c}$, so it identifies
$\mathcal L_{\psi^{-1}}=\mathcal L_{\psi^{-1},x}$ with $\mathcal L_{\psi,-x}$
([lem-fd-as-characters]), and it fixes the root $0$. Pulling $\mu$ back
along $x\mapsto(x,-x)$ gives
$\mathcal L_{\psi,x}\otimes\mathcal L_{\psi,-x}\cong\mathcal L_{\psi,0}$, and
$\mathcal L_{\psi,0}$ is trivialized globally by evaluation at the section
$y=0$ of the split cover $y^q-y=0$. The resulting perfect pairing of lisse
rank-one sheaves ([lem-fd-as-lisse]) is $\delta$, and at the origin it is
$\varepsilon\otimes\varepsilon$ by construction. The same constructions
for $X_0$ and $f$ are the pullbacks along $f$. The comparison with the
$\mathbf F_p$-model is [lem-wft-as-comparison] (3).
