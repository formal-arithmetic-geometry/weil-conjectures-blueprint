+++
kind  = "proof"
of    = "lem-sfb-grothendieck-k-injective"
+++
This is the theorem of Alonso Tarrío, Jeremías López and Souto Salorio, and of Serpé
(see the chapter on injectives of the Stacks Project, section on K-injective
embeddings). Fix a generator $U$ of $\mathcal C$ and a regular cardinal $\kappa$, and
call an object *small* if it is a quotient of a coproduct of fewer than $\kappa$ copies
of $U$. For $\kappa$ large enough, every acyclic complex is the $\kappa$-filtered union of
its acyclic subcomplexes with small terms. Consider, up to isomorphism, the set of
inclusions $A\to B$ of complexes with $B$ having small terms and $B/A$ acyclic. The small
object argument, run on this set, embeds $K$ by a monomorphic quasi-isomorphism into a
complex $I$ that has the right lifting property against all such inclusions. The argument
uses that filtered colimits in $\mathcal C$ are exact, so that transfinite compositions of
monomorphic quasi-isomorphisms are again monomorphic quasi-isomorphisms. By the lifting
property, every map from an acyclic complex to $I$ extends along the inclusion into the
cone of the identity, so it is null-homotopic. Hence $I$ is K-injective.
