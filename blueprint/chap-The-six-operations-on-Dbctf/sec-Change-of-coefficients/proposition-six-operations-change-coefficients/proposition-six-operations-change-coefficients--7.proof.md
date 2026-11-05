+++
kind = "proof"
of = "proposition-six-operations-change-coefficients--7"
order = 645015
uses = ["lemma-change-coefficients-internal-hom", "proposition-inverting-ell", "proposition-dctf-x-qbar-2-colimit", "proposition-six-operations-change-coefficients--13"]
+++
For reduction modulo $\ell^n$, the quotient has the two-term finite free resolution given by multiplication by $\ell^n$. The projection formula and dualizability of this quotient complex show that derived extension of scalars commutes with internal Hom.

For $\mathcal O_E\to E$, take the mate of the tensor comparison under rationalization. For $E\to F$, use a finite basis to identify scalar extension with a finite sum on the ambient derived categories; the resulting adjunction proves the internal-Hom comparison invertible. Pass to $E\to\Qbarl$ using the filtered $2$-colimit. Finally use [proposition-six-operations-change-coefficients--13] to compose the comparisons for $\mathcal O_E\to E\to\Qbarl$.
