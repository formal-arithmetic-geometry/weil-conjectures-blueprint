+++
kind = "proof"
of = "lem-weil-pbc-free-resolution-ses-split"
+++
*Step 1 (one stage).* For a short exact sequence $0\to Q\xrightarrow{u}Q'\xrightarrow{v}Q''\to0$, let $P$ and $T$ be the free modules on the sets $Q$ and $Q''$, with surjections $\eta:P\to Q$, $\theta:T\to Q''$, and choose a linear lift $\lambda:T\to Q'$ of $\theta$ (send each basis element to a preimage under $v$). Define $\mu:P\oplus T\to Q'$ by $\mu(x,z)=u(\eta(x))+\lambda(z)$; it is surjective. Then $0\to P\to P\oplus T\to T\to0$ is split exact, with $\mu(x,0)=u(\eta(x))$ and $v(\mu(x,z))=\theta(z)$.

*Step 2 (kernels).* The maps $x\mapsto(x,0)$ and $(x,z)\mapsto z$ restrict to a short exact sequence $0\to\ker\eta\to\ker\mu\to\ker\theta\to0$: injectivity is clear; if $(x,0)\in\ker\mu$ then $\eta(x)=0$ by injectivity of $u$, giving exactness in the middle; and for $z\in\ker\theta$, exactness of the original sequence gives $a\in Q$ with $u(a)=-\lambda(z)$, and choosing $x$ with $\eta(x)=a$ gives $(x,z)\in\ker\mu$ over $z$.

*Step 3 (recursion).* Apply Step 1 to the original sequence and then recursively to the kernel sequence of Step 2. In degree $n$ this gives $F_n=P$, $F'_n=P\oplus T$, $F''_n=T$ of the $n$-th stage, with differentials the next-stage surjection followed by the kernel inclusion; their ranges and kernels agree with the kernels of the previous stage, so the three augmented complexes are exact. The inclusion and projection are chain maps, the augmentation squares commute by the formulas in Step 1, and the first projection $\pi_n$ and second inclusion $s_n$ give the splittings, with the four identities checked on components.
