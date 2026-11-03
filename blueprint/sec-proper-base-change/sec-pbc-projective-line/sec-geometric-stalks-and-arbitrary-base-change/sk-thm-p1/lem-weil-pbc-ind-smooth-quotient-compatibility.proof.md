+++
kind = "proof"
of = "lem-weil-pbc-ind-smooth-quotient-compatibility"
+++
Put J = I.map(algebraMap R Λ) and L = K.map(algebraMap R Λ). Monotonicity gives L ≤ J. The ideal extended from I.map(Quotient.mk K) to Λ/L equals J.map(Quotient.mk L): ideal map composition and commutativity of the quotient algebra square give the equality. DoubleQuot.quotQuotEquivQuotOfLE identifies (R/K)/(I/K) with R/I and (Λ/L)/(J/L) with Λ/J. These maps send the double class of each element to its single class, so they commute with the structure maps.

Restrict scalar actions along the base ring isomorphism and its inverse. On algebra homomorphisms keep the underlying functions; scalar compatibility follows by substitution. These functors are inverse up to the identity maps on underlying rings. Smoothness is preserved: transport a finite polynomial presentation by changing coefficients along the isomorphism, and transport the square-zero lifting problem along the same scalar action; the original lift is a lift after transport. Thus both finite presentation and formal smoothness hold for each transported term.

Apply the transport functor to the given diagram and its colimit cocone, keeping the same small filtered index category. It remains a colimit: send any competing cocone through the inverse functor, use the original universal property, and transport its unique map back. Compose the transported vertex with the compatible algebra isomorphism from the first step. The resulting cocone has the required double quotient as vertex and smooth terms, hence witnesses ObjectProperty.ind.
