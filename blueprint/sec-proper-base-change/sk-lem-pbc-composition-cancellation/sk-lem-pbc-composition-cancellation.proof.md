+++
kind = "proof"
of = "sk-lem-pbc-composition-cancellation"
uses = ["sk-thm-iff", "sk-prop-pbc-degree-zero", "sk-thm-groth-ss"]
+++
We use [sk-thm-iff]. Fix a prime $r$ and an arbitrary base change
$c:Z'\to Z$. Write $a:X'\to X$ and $b:Y'\to Y$ for the projections, and
$u':X'\to Y'$, $v':Y'\to Z'$ for the induced maps. Since inverse image of
constant-coefficient module sheaves is exact, its right adjoint $u_*$
preserves injectives. Thus the Grothendieck spectral sequence for direct
images ([sk-thm-groth-ss]; Stacks Project, Tag 0734) is available:

$$
R^pv'_*R^qu'_*a^{-1}J\ \Longrightarrow\ R^{p+q}(v'u')_*a^{-1}J.
$$

It is a first-quadrant spectral sequence, natural in the sheaf $J$.

*(1)* Let $J$ be injective among $\mathbf F_r$-module sheaves on $X$. The
condition $\mathrm{IA}_r(u)$ gives $R^qu'_*a^{-1}J=0$ for $q>0$. Degree-zero
proper base change [sk-prop-pbc-degree-zero] identifies, as sheaves of
$\mathbf F_r$-modules on $Y'_{\Et}$,

$$
u'_*a^{-1}J\simeq b^{-1}u_*J.
$$

The sheaf $u_*J$ is injective, so $\mathrm{IA}_r(v)$ kills
$R^pv'_*b^{-1}u_*J$ for $p>0$. Thus the spectral sequence gives
$R^m(v'u')_*a^{-1}J=0$ for $m>0$. This proves $\mathrm{IA}_r(vu)$ for every
$r$, and hence (1).

*(2)* Let $I$ be injective among $\mathbf F_r$-module sheaves on $Y$. Choose a
monomorphism of sheaves $u^{-1}I\hookrightarrow J$ with $J$ injective on $X$,
and let $\iota:I\to u_*J$ be its adjoint. This is a global sheaf morphism. It
is monic: for a geometric point $\bar y$ choose a geometric point $\bar x$
above it, which exists by surjectivity of $u$. The composite

$$
I_{\bar y}\xrightarrow{\ \iota_{\bar y}\ }(u_*J)_{\bar y}\longrightarrow J_{\bar x}
$$

is the stalk of the chosen monomorphism, under $(u^{-1}I)_{\bar x}=I_{\bar y}$,
so it is injective. Injectivity of $I$ now supplies a sheaf map
$s:u_*J\to I$ satisfying $s\iota=\mathrm{id}_I$. Thus $I$ is a direct summand
of $u_*J$.

The assumptions on $u$ and $vu$ give

$$
R^qu'_*a^{-1}J=0\quad(q>0),\qquad R^m(v'u')_*a^{-1}J=0\quad(m>0).
$$

The spectral sequence collapses to its $q=0$ row and gives

$$
R^pv'_*b^{-1}u_*J\simeq R^pv'_*u'_*a^{-1}J=0\qquad(p>0).
$$

The splitting of $I\to u_*J$ remains a splitting after $b^{-1}$. Higher
direct image preserves finite direct sums and their direct summands, so
$R^pv'_*b^{-1}I=0$ for $p>0$. This proves $\mathrm{IA}_r(v)$, and (2) follows
for all primes $r$.
