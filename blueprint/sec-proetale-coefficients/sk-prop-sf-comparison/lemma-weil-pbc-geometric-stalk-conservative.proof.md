+++
kind  = "proof"
of    = "lemma-weil-pbc-geometric-stalk-conservative"
+++
Write $\underline F$, $\underline G$ for the sheaves of sets obtained by
composing $F$, $G$ with the forgetful functor of $\mathcal A$; they are
sheaves by the compatibility of the forgetful functor with the sheaf
condition, and $\varphi$ induces $\underline\varphi:\underline F\to\underline G$.
A geometric stalk is a colimit over the opposite of the cofiltered category of
pointed etale neighbourhoods [def-weil-pbc-geometric-stalks], i.e. a filtered
colimit, and the forgetful functor preserves filtered colimits; so the
underlying set of $F_{\bar s}$ is the stalk $\underline F_{\bar s}$, and
$\underline\varphi_{\bar s}$ is a bijection for every $s\in S$. Passing to a
larger universe of sets does not change these stalks
([lemma-openclosed-point-ulift]).

Let $u:U\to S$ be etale and $x\in U$ with $s=u(x)$. Since $\kappa(x)$ is a
finite separable extension of $\kappa(s)$, it embeds over $\kappa(s)$ into the
algebraic closure $\overline{\kappa(s)}$ (which is in particular separably
closed, [def-kun-separably-closed]); this gives a geometric point $\bar x$ of
$U$ at $x$ lying over $\bar s$, so $(U,\bar x)$ is a pointed etale
neighbourhood of $\bar s$.

*Injectivity on sections.* Let $a,b\in\underline F(U)$ with
$\underline\varphi(a)=\underline\varphi(b)$. For each $x\in U$ as above, the
germs of $a$ and $b$ in $\underline F_{\bar s}$ have the same image under the
bijection $\underline\varphi_{\bar s}$, so they agree; hence $a$ and $b$
agree on some pointed etale neighbourhood $(V_x,\bar v_x)\to(U,\bar x)$. The
images of the $V_x\to U$ contain every point of $U$, so $\{V_x\to U\}$ is an
etale covering, and $a=b$ by the sheaf axiom.

*Surjectivity on sections.* Let $c\in\underline G(U)$. For each $x\in U$ the
germ of $c$ at $\bar s$ (through $(U,\bar x)$) is the image of a germ of
$\underline F$, so there are a pointed etale neighbourhood
$(V_x,\bar v_x)\to(U,\bar x)$ and $a_x\in\underline F(V_x)$ with
$\underline\varphi(a_x)=c|_{V_x}$. On $V_x\times_UV_{x'}$, which is etale over
$S$, the restrictions of $a_x$ and $a_{x'}$ have the same image $c$, so they
agree by injectivity. As $\{V_x\to U\}$ is an etale covering, the $a_x$ glue
to $a\in\underline F(U)$, and $\underline\varphi(a)=c$ by the sheaf axiom for
$\underline G$.

Hence the underlying map of sets of $\varphi_U:F(U)\to G(U)$ is bijective for
every etale $U\to S$. The forgetful functor reflects isomorphisms, so every
$\varphi_U$ is an isomorphism in $\mathcal A$, and $\varphi$ is an isomorphism
of sheaves.
