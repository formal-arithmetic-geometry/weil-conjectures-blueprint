+++
kind  = "proof"
of    = "lem-a1-artin-schreier-ramified-infinity"
+++
By [lem-fd-as-cover], $\pi$ is finite etale of degree $p$ with
automorphism group $\mathbf F_p$ acting by $\sigma_c$, and by
[lem-fd-as-characters] its $\Psi$-isotypic part is lisse of rank one.

Let $R$ be the strict henselization of $\mathcal O_{\mathbf P^1_k,\infty}$,
with residue field $k$, uniformizer $t=1/x$ and fraction field $K$;
let $\overline K$ be an algebraic closure. Since $k$ is algebraically
closed, the inertia group of [d-real-boundary] at $\infty$ is
$I_\infty=\operatorname{Gal}(\overline K/K)$, acting on the geometric
generic stalk at $\operatorname{Spec}\overline K\to\mathbf A^1$.

*The stalk.* Over $\operatorname{Spec}\overline K$ the fibre of $\pi$ is
the set $\mathcal R$ of roots of $u^p-u=a/t$ in $\overline K$; it has
$p$ elements (the derivative is $-1$) and is a torsor under
$\mathbf F_p$ by translation. By [lemma-weil-pbc-finite-stalk-formula],
$(\pi_*\Qlb)_{\bar\eta}$ is the space of functions
$\mathcal R\to\Qlb$, with $\sigma_c$ and $g\in I_\infty$ acting
through their actions on $\mathcal R$. Fix $u_0\in\mathcal R$ and write
$g(u_0)=u_0+\kappa(g)$ with $\kappa(g)\in\mathbf F_p$. Since $g$ fixes
$\mathbf F_p$, $g(u_0+c)=u_0+c+\kappa(g)$, so $g$ acts on $\mathcal R$
as the translation by $\kappa(g)$, and $\kappa$ is a homomorphism.
Hence $g$ acts on $(\pi_*\Qlb)_{\bar\eta}$ as $\sigma_{\pm\kappa(g)}$
(the sign is fixed by the convention for the induced action on
functions). From $\sigma_be_\Psi=\Psi(b)e_\Psi$ it follows that $g$
acts on the line $(\mathcal L_{\psi(ax)})_{\bar\eta}$ by the scalar
$\Psi(\pm\kappa(g))$.

*The cover is totally ramified.* Put $L=K(u_0)$, so $[L:K]\leq p$.
Since $K$ is henselian, its valuation extends uniquely to $L$; let
$v_L$ be the extension normalized with value group $\mathbf Z$, and
put $e=v_L(t)\geq1$, so $e\leq[L:K]$. As $a$ is a unit,
$v_L(a/t)=-e<0$. If $v_L(u_0)\geq0$ then $v_L(u_0^p-u_0)\geq0$, a
contradiction; so $v_L(u_0)<0$, whence $v_L(u_0^p)<v_L(u_0)$ and
$p\,v_L(u_0)=v_L(u_0^p-u_0)=-e$. Thus $p\mid e$, and
$e\leq[L:K]\leq p$ forces $e=[L:K]=p$. In particular
$u_0\notin K$, so some $g\in I_\infty$ moves $u_0$, and $\kappa$ is
surjective onto $\mathbf F_p$.

*Conclusion.* The nontrivial character $\Psi$ of the group
$\mathbf F_p$ of prime order is injective, so
$g\mapsto\Psi(\pm\kappa(g))$ is a character of $I_\infty$ of exact
order $p$. Inertia at infinity therefore acts nontrivially on the
geometric generic stalk: $\mathcal L_{\psi(ax)}$ is ramified at
infinity.
