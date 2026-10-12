+++
kind  = "proof"
of    = "sk-def-sfb-ring-object"
+++
**1.** Multiplication $R\times R\to R$ is $\mathbf Z$-bilinear, so it induces
$\mu\colon R\otimes_{\mathbf Z}R\to R$. Under $\mathbf Z\otimes_{\mathbf Z}R\cong R$, the
composite $\mu\circ(\eta\otimes\mathrm{id})$ sends $n\otimes b$ to $nb$, so it is the
left unitor. The right unitor is treated in the same way. Associativity of $\mu$ is
checked on pure tensors $a\otimes b\otimes c$, where it is associativity of the ring
multiplication. A ring homomorphism $f$ satisfies $f(ab)=f(a)f(b)$ and $f(1)=1$, which
says that $f$ commutes with $\mu$ and with $\eta$. If $R$ is commutative, then
$\mu(b\otimes a)=ba=ab$, so $\mu\circ\beta_{R,R}=\mu$.

**2.** The monoidal structure on abelian presheaves is objectwise. So a ring object of
abelian presheaves is the same as a functor from $C^{\mathrm{op}}$ to ring objects of
$\Ab$, with multiplication and unit given objectwise. By 1, $P$ is such a functor, and
a natural transformation of presheaves of rings is objectwise a morphism of ring
objects. Sheafification $a$ is strong monoidal and braided by
[sk-def-sfb-sheaf-tensor]. A strong monoidal functor carries a ring object
$(M,\mu,\eta)$ to the ring object $aM$, with multiplication
$aM\otimes aM\cong a(M\otimes M)\xrightarrow{a\mu}aM$ and unit
$\mathbf 1\cong a\mathbf 1\xrightarrow{a\eta}aM$. A braided one preserves commutativity.
Applying this to $P$ gives the ring object $aP$.

**3.** Forgetting from rings to abelian groups preserves limits, so the abelian presheaf
underlying $\mathcal R$ is a sheaf $\mathcal R_{\Ab}$. Since $\mathcal R_{\Ab}$ is a
sheaf, the counit $a(\mathcal R_{\Ab})\to\mathcal R_{\Ab}$ is an isomorphism. By 2,
$a(\mathcal R_{\Ab})$ is a ring object. Transport its ring object structure, and
commutativity, along this isomorphism. For a morphism $f\colon\mathcal R\to\mathcal R'$
of sheaves of rings, the underlying morphism of abelian sheaves is $a(f)$ conjugated by
the two counit isomorphisms, by naturality of the counit. Here $a(f)$ is a morphism of
ring objects by 2, and so are the two isomorphisms, by construction of the transported
structures. Hence $f$ is a morphism of ring objects.
