+++
kind = "proof"
of = "sk-lem-proper-unbounded-window"
uses = ["sk-lem-proper-heart-bound", "sk-prop-ind-heart", "sk-prop-pe-left-complete", "sk-prop-pe-milnor"]
+++
*Bounded below $K$.* The hypercohomology spectral sequence

$$
E_2^{u,v}=R^up_*\mathcal H^v(K)\Longrightarrow\mathcal H^{u+v}(Rp_*K)
$$

converges. By [sk-lem-proper-heart-bound] its only nonzero columns are $0\leq u\leq2d+1$, and their terms
lie in $\IndCons(Y,\Lambda)$. So each $\mathcal H^n(Rp_*K)$ has a finite filtration whose graded pieces are
subquotients of objects of $\IndCons(Y,\Lambda)$; since this category is closed under kernels, cokernels
and extensions ([sk-prop-ind-heart]), $\mathcal H^n(Rp_*K)\in\IndCons(Y,\Lambda)$. The two amplitude bounds
can be read off from the columns ([det-proper-unbounded-window-bounded-below]).

*Arbitrary $K$.* By [sk-prop-pe-left-complete], $K\simeq R\varprojlim_n\tau_{\geq-n}K$. Being a right
adjoint, $Rp_*$ preserves products and hence derived inverse limits, so
$Rp_*K\simeq R\varprojlim_nRp_*\tau_{\geq-n}K$. The fibre of $\tau_{\geq-n-1}K\to\tau_{\geq-n}K$ is
$\mathcal H^{-n-1}(K)[n+1]$, whose direct image has cohomology only in degrees $[-n-1,2d-n]$. Hence, for
fixed $q$, the towers $\mathcal H^q(Rp_*\tau_{\geq-n}K)$ and $\mathcal H^{q-1}(Rp_*\tau_{\geq-n}K)$ have
isomorphisms as transition maps for $n$ large. An eventually constant tower has vanishing
$\varprojlim^1$, so the Milnor sequence of [sk-prop-pe-milnor] gives

$$
\mathcal H^q(Rp_*K)\simeq\mathcal H^q(Rp_*\tau_{\geq-n}K)\quad\text{for all sufficiently large }n.
$$

The right side is covered by the bounded-below case. This proves $\mathcal H^q(Rp_*K)\in\IndCons(Y,\Lambda)$,
and if $K\in\Dic^{\leq b}(X,\Lambda)$ it gives the bound $b+2d+1$. The lower bound needs no argument for
unbounded $K$, since an object of $\Dic^{\geq a}$ is bounded below ([det-proper-unbounded-window-arbitrary]).

*The window isomorphism.* Apply the bounds to the truncation triangles

$$
\tau_{\leq q}K\to K\to\tau_{\geq q+1}K,\qquad
\tau_{\leq q-2d-2}K\to\tau_{\leq q}K\to\tau_{\geq q-2d-1}\tau_{\leq q}K.
$$

The direct image of $\tau_{\geq q+1}K$ lives in degrees $\geq q+1$, and that of $\tau_{\leq q-2d-2}K$ in
degrees $\leq q-1$. The long exact cohomology sequences of the two triangles therefore give isomorphisms
$\mathcal H^q(Rp_*\tau_{\leq q}K)\simeq\mathcal H^q(Rp_*K)$ and
$\mathcal H^q(Rp_*\tau_{\leq q}K)\simeq\mathcal H^q(Rp_*\tau_{\geq q-2d-1}\tau_{\leq q}K)$
([det-proper-unbounded-window-iso]).
