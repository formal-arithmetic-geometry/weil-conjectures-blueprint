+++
kind = "proof"
of = "lem-weil-pbc-jacobi-zariski-left-term-vanishing"
+++
For the canonical presentation $A[B]\to B$, $H_1(L_{B/A})$ is the kernel of the conormal differential $\delta$. The hypothesis $H_1(L_{B/A})=0$ therefore makes $\delta$ injective. The sequence $N_1\xrightarrow{\delta}N_0\to\Omega_{B/A}\to0$ is exact (the image of $\delta$ is the kernel of $N_0\to\Omega_{B/A}$, $\mathrm d[b]\mapsto\mathrm db$), and its last arrow is surjective. Consequently $0\to N_1\to N_0\to\Omega_{B/A}\to0$ is a short exact sequence.

The projective module $\Omega_{B/A}$ is flat. Since the third term of the short exact sequence of the preceding step is flat, the sequence stays exact after tensoring with any module, here $C=B/\mathfrak a$ (by the Tor long exact sequence, with $\operatorname{Tor}_1^B(\Omega_{B/A},C)=0$). It follows that $\delta\otimes\mathrm{id}_C$ is injective, so its kernel is zero. Because $H_1(L_{B/A})$ was already zero, there is no need to factor $\delta$ through its image, to prove that image flat, or to use freeness of $N_0$.

The tensor product $H_1(L_{B/A})\otimes_BC$ is the zero module, as a tensor product with the zero module. The map $H_1(L_{B/A})\otimes_BC\to N_1\otimes_BC$ induced by the kernel inclusion has zero source, hence is injective and is the zero map; its image is the zero submodule, which equals $\ker(\delta\otimes\mathrm{id}_C)$ by the preceding step. Both modules being zero, they are isomorphic, which establishes every part of the conclusion.
