+++
kind = "proof"
of = "det-def-sfb-sheaf-tensor-structure"
+++
For a finite family of presheaves $F_1,\dots,F_n$, every iterated sheaf tensor product of the
$aF_\nu$ (any bracketing, with units inserted) receives a canonical map from the iterated
objectwise tensor product of the $F_\nu$ with the same bracketing, built from units of $a$; by
[det-def-sfb-sheaf-tensor-local-iso] (applied repeatedly, using 2 for the inner factors) it
becomes an isomorphism after sheafification. Call these the *canonical isomorphisms*
$a(F_1\otimes_p\dots\otimes_pF_n)\cong aF_1\otimes\dots\otimes aF_n$.

By construction, each structure map of $\Sh(C,\mathcal A)$ (associator, unitors, symmetry) is
the conjugate of $a$ of the corresponding objectwise structure map by canonical isomorphisms.
Every composite of structure maps occurring in the pentagon, triangle and hexagon identities is
therefore the conjugate of $a$ of the corresponding composite of objectwise structure maps, by
the canonical isomorphisms at its two ends; the intermediate canonical isomorphisms cancel
because they are all induced by units of $a$, and the units are natural. Since the identities
hold objectwise ([det-def-sfb-sheaf-tensor-presheaf]), they hold for sheaves. Similarly
$\beta_{\mathcal G,\mathcal F}\circ\beta_{\mathcal F,\mathcal G}=\mathrm{id}$ because it holds
objectwise. Naturality of all structure maps follows from naturality of the units.

The structure isomorphisms of $a$ are the canonical isomorphisms for $n=2$ and $n=0$. The
compatibility of $a$ with associators, unitors and symmetries is again the statement that the
sheaf structure maps are conjugates of $a$ of the presheaf ones by canonical isomorphisms, which
holds by definition. So $a$ is strong symmetric monoidal.

For $\mathcal A=\Ab$, the definitions specialize to the sheafified objectwise
$\otimes_{\mathbf Z}$, and $a(\underline{\mathbf Z})$ is by definition the constant sheaf
$\underline{\mathbf Z}$.
