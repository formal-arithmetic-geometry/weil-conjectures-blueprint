+++
kind = "proof"
of = "pur7710-lem-residue-detection"
uses = ["pur7710-lem-residue-extension-restriction"]
+++
By Lemma [pur7710-lem-residue-extension-restriction], the hypothesis says that $M\otimes^L_{\mathcal O_E/\varpi^n}\mathcal O_E/\varpi=0$ in $D(\mathsf{Mod}_{\mathcal O_E/\varpi^n})$. The ideals $\varpi^i(\mathcal O_E/\varpi^n)$, $0\leq i\leq n$, form a finite filtration ending in zero, whose successive quotients are $\mathcal O_E/\varpi$-modules isomorphic to $\mathcal O_E/\varpi$. Tensoring $M$ with each quotient therefore gives zero. Tensor the short exact sequences $0\to\varpi^{i+1}\to\varpi^i\to\varpi^i/\varpi^{i+1}\to0$ with $M$; descending induction on $i$, starting from $\varpi^n(\mathcal O_E/\varpi^n)=0$, and the distinguished triangles show that $M\otimes^L_{\mathcal O_E/\varpi^n}\varpi^i(\mathcal O_E/\varpi^n)=0$ for every $i$. For $i=0$ this is $M\otimes^L_{\mathcal O_E/\varpi^n}\mathcal O_E/\varpi^n\cong M$. For $n=1$ the residue extension is the identity and the argument is the same.
