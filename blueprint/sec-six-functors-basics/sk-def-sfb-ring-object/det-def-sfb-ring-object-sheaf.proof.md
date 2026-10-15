+++
kind = "proof"
of = "det-def-sfb-ring-object-sheaf"
+++
The forgetful functor from rings to abelian groups preserves limits, so the sheaf condition for
$\mathcal R$ (a limit condition) gives the sheaf condition for $\mathcal R_{\Ab}$. As
$\mathcal R_{\Ab}$ is a sheaf, the counit $\epsilon\colon a(\mathcal R_{\Ab})\to\mathcal R_{\Ab}$ is
an isomorphism. Transport the ring object structure of $a(\mathcal R_{\Ab})$
([det-def-sfb-ring-object-presheaf]) along $\epsilon$: put
$\mu:=\epsilon\circ\mu_{a\mathcal R}\circ(\epsilon^{-1}\otimes\epsilon^{-1})$ and
$\eta:=\epsilon\circ\eta_{a\mathcal R}$. The axioms are preserved under conjugation by an
isomorphism, and this is the unique structure making $\epsilon$ a morphism of ring objects. By
construction $\mu_{a\mathcal R}=a(\mu_p)$ for the objectwise multiplication $\mu_p$, so the
composite of $\mu$ with the unit $\mathcal R_{\Ab}\otimes_p\mathcal R_{\Ab}\to a(\mathcal R_{\Ab}\otimes_p\mathcal R_{\Ab})$
is $\mu_p$, by naturality of the units and counits of $a$; uniqueness of such an extension holds
because $\mathcal R_{\Ab}$ is a sheaf. The same applies to $\eta$. Commutativity is transported.

For a morphism $f\colon\mathcal R\to\mathcal R'$ of sheaves of rings, naturality of the counit gives
$f=\epsilon'\circ a(f)\circ\epsilon^{-1}$. Here $a(f)$ is a morphism of ring objects by
[det-def-sfb-ring-object-presheaf] and $\epsilon$, $\epsilon'$ are isomorphisms of ring objects, so
$f$ is a morphism of ring objects.
