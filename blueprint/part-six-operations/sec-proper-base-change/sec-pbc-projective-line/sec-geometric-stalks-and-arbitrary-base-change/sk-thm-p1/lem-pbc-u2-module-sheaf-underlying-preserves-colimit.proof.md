+++
kind = "proof"
of = "lem-pbc-u2-module-sheaf-underlying-preserves-colimit"
+++
Let $U$ be the forgetful functor from $\Lambda$-modules to abelian groups. It preserves limits and filtered colimits, so sheafification commutes with $U$: forgetting the module structure of a presheaf and then sheafifying as abelian presheaf is naturally isomorphic to sheafifying as presheaf of $\Lambda$-modules and then forgetting.

Forgetting on presheaves preserves colimits, since colimits of presheaves are computed objectwise and $U$ preserves colimits; abelian sheafification preserves colimits as a left adjoint. By the natural isomorphism above, the composite of module sheafification with the sheaf-level forgetful functor preserves colimits.

A colimit of a diagram of sheaves of $\Lambda$-modules is the sheafification of its presheaf colimit, and the inclusion of sheaves into presheaves is fully faithful. Hence the sheaf-level forgetful functor preserves colimits of every small diagram.
