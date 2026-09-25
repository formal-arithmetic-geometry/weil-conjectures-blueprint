+++
id = "prop-pod-verdier-dual-on-smooth"
kind = "theorem"
title = "Verdier dual of a perfect complex on a smooth scheme"
order = 2380
tags = ["latex:proposition"]
uses = ["cor-pur-adic-and-rational-smooth-dualizing-complexes", "cor-pur-finite-stage-smooth-dualizing-complex", "def-pod-coefficient-dual-on-x", "def-pod-conventions", "def-weil-derived-pullback-tensor-hom", "lem-pod-twist-interchange"]
+++
In the Poincare duality conventions of this chapter (the fixed setting), let $K\in D^b_{ctf}(X,\Lambda)$ be perfect over $\Lambda_X$. The smooth dualizing-complex identification of the purity chapter

$$
\omega _{X,\Lambda }\xrightarrow {\  \sim \  }\Lambda _X(d)[2d]
$$

(at the $E$- and $\overline{\mathbf Q}_{\ell }$-stages its transport) and the twist interchange of Lemma 9.15 give a canonical isomorphism

$$
\mathbb D_XK\xrightarrow {\  \sim \  }K^\vee (d)[2d],
$$

natural in $K$, compatible with finite reduction, scalar extension, shifts, and the canonical evaluation.

## Proof

Step 1: the definition. By definition, $\mathbb D_XK=R\mathcal Hom_X(K,\omega _{X,\Lambda })$, with $\omega _{X,\Lambda }=Ra_X^!\Lambda$ the dualizing complex of the conventions of [def-pod-conventions]. Step 2: the smooth purity input. The smooth dualizing-complex identification of [cor-pur-finite-stage-smooth-dualizing-complex] (at the finite stage $A=A_{E,n}$) and its transport [cor-pur-adic-and-rational-smooth-dualizing-complexes] (at the $\mathcal O_E$-, $E$-, and $\overline{\mathbf Q}_{\ell }$-stages) provide the canonical orientation

$$
\eta _X:\omega _{X,\Lambda }\xrightarrow {\  \sim \  }\Lambda _X(d)[2d],
$$

compatible with finite reduction, scalar extension, and shifts. Step 3: substitution and interchange. Substituting $\eta _X$ into the internal Hom and using the shift of the second variable,

$$
\mathbb D_XK\cong R\mathcal Hom_X\bigl(K,\Lambda _X(d)[2d]\bigr) \cong \bigl(R\mathcal Hom_X(K,\Lambda _X(d))\bigr)[2d] \cong K^\vee (d)[2d],
$$

the second isomorphism being the shift axiom of the derived internal Hom of [def-weil-derived-pullback-tensor-hom], the third being [lem-pod-twist-interchange] with $m=d$ (its hypothesis is the perfectness of $K$ over $\Lambda _X$, part of the statement), and where $K^\vee =R\mathcal Hom_X(K,\Lambda _X)$ is the coefficient dual of [def-pod-coefficient-dual-on-x]. Step 4: the canonicality. The composite is canonical because its two ingredients are: the orientation is the canonical one of the purity chapter, and the twist interchange and the shift identification are the canonical maps of the adjunction (they are natural in $K$, on the generators $K=\Lambda _X^r$ they are the coordinate isomorphisms, and the index of the shift is the fixed constant $2d$). Step 5: the compatibilities. The naturality in $K$, and the compatibility with finite reduction, scalar extension, and shifts, follow from the corresponding properties of the two ingredients, recorded in [cor-pur-finite-stage-smooth-dualizing-complex], [cor-pur-adic-and-rational-smooth-dualizing-complexes], and [lem-pod-twist-interchange]. The compatibility with the canonical evaluation is the compatibility of the twist interchange with the tensor–internal-Hom adjunction of [def-weil-derived-pullback-tensor-hom] (the evaluation is the counit, and the interchange maps the counit of $K\otimes ^L\Lambda _X(d)$ to the counit of $K$ tensored with the identity of $\Lambda _X(d)$, after the tensor of $K^\vee (d)\otimes \Lambda _X(d)\cong K^\vee \otimes \Lambda _X(d)^2$ is unwound through the associativity and commutativity coherence of the derived tensor product).
