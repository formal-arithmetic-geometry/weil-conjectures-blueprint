+++
kind  = "proof"
of    = "det-l-dl-general-excision"
+++
By [sk-r-real-linear], mixed sheaves of weights at most $u$ are closed
under subquotients and extensions. Hence, if $A\to B\to C$ is exact and
$A,C$ have this bound, so does $B$, an extension of a quotient of $A$
by a subobject of $C$.

*Source.* Apply $Rf_{0!}$ to
$j_{0!}j_0^*K\to K\to i_{0*}i_0^*K\xrightarrow{+1}$
([sk-prop-sf-open-closed-triangle]) and use the composition
isomorphism of [sk-thm-sf-comp-composition]. In the
Frobenius-equivariant cohomology sequence, the term of degree $n$ is an
extension of subquotients of the two outer terms in the same degree;
both have the required bound, since restrictions preserve weights.

*Target.* Compact-support base change [sk-prop-sf-cbc] identifies the
restrictions of $Rf_{0!}K$ to $V_0$ and $T_0$ with the direct images
of the restricted complexes. Extension by zero and closed direct image
preserve pure weights, so the same triangle on $Y_0$ gives the bound.
Filtrations of the coefficient sheaf are handled by the corresponding
long exact sequences. The details are
[lem-zl-morphism-open-closed-reduction].
