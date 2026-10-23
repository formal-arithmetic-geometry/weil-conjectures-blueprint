+++
kind = "proof"
of = "lem-weil-pbc-constant-module-sheaves-forget-colimits"
+++
For a commutative ring $\Lambda$, restriction of scalars along $\mathbf Z\to\Lambda$ is left adjoint to coextension of scalars, and $\mathbf Z$-modules are the same as abelian groups; so the functor $\mathrm{Mod}_\Lambda\to\mathrm{Ab}$ forgetting the scalars is a left adjoint.

Composing a presheaf with this functor and then sheafifying is therefore a left adjoint on sheaves (its right adjoint is composition with the right adjoint coefficient functor). Forgetting the scalars of a module-valued sheaf already gives a sheaf (the sheaf condition is a limit condition on underlying sets, and the forgetful functor preserves limits), so this compose-and-sheafify functor is naturally isomorphic to $V$. Hence $V$ is a left adjoint, and left adjoints preserve all colimits, in particular colimits indexed by categories in universe $u+1$, with their canonical cocones.
