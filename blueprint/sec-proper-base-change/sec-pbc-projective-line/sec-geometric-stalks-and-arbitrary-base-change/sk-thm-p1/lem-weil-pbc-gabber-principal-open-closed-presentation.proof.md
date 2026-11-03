+++
kind = "proof"
of = "lem-weil-pbc-gabber-principal-open-closed-presentation"
uses = ["def-pc-separably-closed"]
+++
Lift $h$ to $f\in R$. If $f=0$, then $D(h)$ is empty and its unique morphism to $\operatorname{Spec}R$ is a closed immersion; take $S=R$.

If $f\neq0$, let $S=R_f$. It is a localization of the normal domain $R$ at a multiplicative set not containing $0$, hence a normal domain with the same fraction field, which is separably closed [def-pc-separably-closed].

The ring map $R_f\to(R/I)_h$ induced by $R\to R/I$ is surjective: every element of $(R/I)_h$ is $\bar b/h^n$ and is the image of $b/f^n$. So $\operatorname{Spec}(R/I)_h\to\operatorname{Spec}R_f$ is a closed immersion, and composing with the isomorphism $D(h)\cong\operatorname{Spec}(R/I)_h$ gives the required closed immersion.
