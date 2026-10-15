+++
kind = "proof"
of = "det-sp-representing-pair-gluing"
uses = ["det-sp-representing-pair-uniqueness", "det-sf-mate-open-restriction"]
+++
Let $M\in\Dctf(X,\Lambda_n)$. The open-cover triangle (the Mayer–Vietoris
triangle of extensions by zero)

$$
j_{U\cap V!}(M|_{U\cap V})\xrightarrow{(1,-1)}j_{U!}(M|_U)\oplus j_{V!}(M|_V)
\xrightarrow{(1,1)}M\longrightarrow
$$

is distinguished: it is the derived form of the exact sequence of sheaves
$0\to j_{U\cap V!}F|_{U\cap V}\to j_{U!}F|_U\oplus j_{V!}F|_V\to F\to0$, which
is exact on stalks. All its terms lie in $\Dctf(X,\Lambda_n)$ (extension by zero
preserves $\Dctf$).

Apply the two cohomological functors $\Hom(-,H)$ and $\Hom(Rf_!(-),K)$ to this
triangle and its rotations. The natural transformation
$\Phi_M:\Hom(M,H)\to\Hom(Rf_!M,K)$, $b\mapsto\varepsilon\circ Rf_!(b)$, gives a
morphism between the resulting long exact sequences (it is natural in $M$ and
commutes with shifts, since $Rf_!$ is exact). For $W$ open, the adjunction
$j_{W!}\dashv j_W^*$ identifies $\Hom(j_{W!}(M|_W),H)=\Hom(M|_W,H|_W)$ and,
using $Rf_!j_{W!}=Rf_{W!}$,
$\Hom(Rf_!j_{W!}(M|_W),K)=\Hom(Rf_{W!}(M|_W),K)$; under these
identifications $\Phi_{j_{W!}(M|_W)}$ becomes $b'\mapsto\varepsilon_W\circ Rf_{W!}(b')$,
because the adjoint of $b'$ is $\text{counit}\circ j_{W!}(b')$. By hypothesis
these maps are bijections for $W=U,V,U\cap V$ and all shifts of $M|_W$ (which
lie in $\Dctf(W,\Lambda_n)$). In the morphism of long exact sequences, the map
at $M$ is flanked by two bijections on each side (the terms for $U\sqcup V$
and $U\cap V$ in adjacent degrees), so it is a bijection by the five lemma.
Hence $(H,\varepsilon)$ is a representing pair. By
[det-sp-representing-pair-uniqueness] it is then canonically isomorphic to
$(f^!K,\varepsilon_K)$ by the counit-preserving isomorphism.
