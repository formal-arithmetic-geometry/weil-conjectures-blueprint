+++
kind = "proof"
of = "det-def-sfb-sheaf-tensor-hom-sheaf"
+++
Let $R$ be a covering sieve on $U$, viewed as a full subcategory of $C/U$ closed under
precomposition. We must show that $[F,G](U)\to\lim_{(v\colon V\to U)\in R}[F,G](V)$ is an
isomorphism. By Yoneda in $\mathcal A$ it suffices to show that it induces a bijection on
$\Hom_{\mathcal A}(A,-)$ for every object $A$.

By the Hom formula of [det-def-sfb-sheaf-tensor-presheaf], $\Hom_{\mathcal A}(A,[F,G](U))$ is
the set of natural families $\varphi_v\colon F(V)\otimes A\to G(V)$ indexed by all of $C/U$. An
element of $\Hom_{\mathcal A}(A,\lim_R[F,G](V))$ is a compatible family, indexed by $v\in R$, of
natural families over $C/V$; since $R$ is a sieve, every $W\to V\to U$ lies in $R$, and
compatibility says the value at $W\to V$ depends only on $W\to U$. So this set is the set of
natural families $\varphi_w$ indexed by $w\in R$ only, and the map in question is restriction of
families from $C/U$ to $R$.

*Injectivity.* Let $\varphi,\varphi'$ be natural families over $C/U$ that agree on $R$, and let
$v\colon V\to U$ be arbitrary. The pullback sieve $v^*R$ covers $V$, and for $w\colon W\to V$ in
$v^*R$ we have $v\circ w\in R$, so by naturality
$G(w)\circ\varphi_v=\varphi_{vw}\circ(F(w)\otimes A)=\varphi'_{vw}\circ(F(w)\otimes A)=G(w)\circ\varphi'_v$.
Since $G$ is a sheaf, $G(V)\to\lim_{w\in v^*R}G(W)$ is an isomorphism, in particular a
monomorphism, so $\varphi_v=\varphi'_v$.

*Surjectivity.* Let $(\varphi_w)_{w\in R}$ be natural. For arbitrary $v\colon V\to U$, the maps
$\varphi_{vw}\circ(F(w)\otimes A)\colon F(V)\otimes A\to G(W)$, $w\in v^*R$, are compatible with
restriction along $v^*R$, by naturality of $\varphi$. As $G(V)\cong\lim_{w\in v^*R}G(W)$, there is
a unique $\tilde\varphi_v\colon F(V)\otimes A\to G(V)$ with
$G(w)\circ\tilde\varphi_v=\varphi_{vw}\circ(F(w)\otimes A)$ for all $w\in v^*R$. If $v\in R$, then
$v^*R$ is the maximal sieve and $\tilde\varphi_v=\varphi_v$ by uniqueness (take $w=\mathrm{id}$).
Naturality of $\tilde\varphi$: for $u\colon V'\to V$, both $G(u)\circ\tilde\varphi_v$ and
$\tilde\varphi_{vu}\circ(F(u)\otimes A)$ have the same restriction
$\varphi_{vuw'}\circ(F(uw')\otimes A)$ to every $w'\in(vu)^*R$, so they agree, again because $G$
is a sheaf. Hence $\tilde\varphi$ is a natural family over $C/U$ extending $\varphi$.
