# Re-review of `wholeblueprint-final.tex` after the audit fixes

Ten read-only reviewers each re-read one slice of the tex. Line numbers refer to the
current, uncommitted file. Nothing below has been fixed yet.

## 1. Audit findings: status

All 53 findings are resolved or have no counterpart in the tex, except:

| # | Status | Where | What remains |
|---|---|---|---|
| 34 | partial | `prop:sf-cbc` (~5755), the Ex_! sentence of `thm:sf-package`(2) | Ex_! is still typed "at every coefficient stage, in the ambient category". For proper f, Ex_! = Ex_*, so the nodal-cubic counterexample with discrete `E` on the étale site still applies. This also contradicts the new closing sentence of clause (2). The adic stages need to be restricted to D^b_c of the pro-étale categories here too. Related: `def:fourier-set` (13097) says "étale sheaves of E-modules", which reads as the discrete model. |
| 50 | partial | `thm:regular` Step 4(iii) (~7238) | Step 4(iii) asserts that smooth purity for the projection 𝔸^c_B→B sends 1 to the Kummer frame class. Nothing proves this. `prop:an` states only the Rz^! form, yet `thm:smooth-purity` and `prop:cohsm` cite it for the Rπ^! form. The `cor:trace` normalization inherits this gap. |
| 40 | partial | `lem:picard-cech-computes` (~2299) | Say "isomorphism of Γ(S,O)-modules". The tangent-space proof relies on that linearity. |
| 20 (six-functor part) | resolved by context | `prop:sf-rf-shriek-preservation`, `thm:sf-ctf-stability`, typing table | The global bounds hold because all schemes are of finite type over k = F̄_q. That is stated only in the chapter conventions and proofs, not in these statements. |

## 2. Problems in the edits made today

| Node | Problem | Fix |
|---|---|---|
| `prop:smooth-proper-purity` Step 3 (~14987) | **Wrong citation.** It combines the absolute Verdier exchange (`thm:sf-verdier-exchange`, uses ω_Y) with the relative dual. That does not work on a singular Y_0. The displayed isomorphism is still true. | Use `thm:sf-tensor-hom` with N=Λ_Y: RHom(Rf_!F,Λ) ≅ Rf_*RHom(F,Rf^!Λ). Then apply the relative θ_{f_0}. Reading off degrees uses that R^if_*F is lisse (Step 1). Add `thm:sf-tensor-hom` to `\uses`. |
| `cor:trace` (~10561) | The claim tr(d)[x⊂X]=1 is right, but the justification "normalized integration map of `thm:purity-transport`" is circular. That phrase is only a name there. The claim is also made at O_E, E, Q̄_ℓ, where [x⊂X] is defined only at finite level. | Argue via `thm:regular`(c) (cl_x = Φ_x), composition of the counits for a_X∘x = id, and smooth purity of id = id. Do it at A_{E,n}, then transport. |
| `thm:picard-duality` (~2495) | **Trace ill-defined for imperfect k.** Tr_{κ(x)/k}∘res_x needs a coefficient field containing k. At inseparable points there is none, and Tr vanishes there. Example: k=F_p(t), x: u^p=t on ℙ¹. Serre GACC covers only algebraically closed k. | Use Tate's residue (1968), or define t_X by base change to k̄, or assume k perfect. |
| `cor:picard-degree-g` (~2604) | Needs the new RR hypothesis H⁰(O)=k. Counterexample: ℙ¹_ℂ over ℝ, K=ℂ. The hypothesis is also not checked at the twist lemma (~2699) or `thm:picard-hilb-curves` (~2923); it holds at all actual uses. | Add "H⁰(X,O_X)=k" (or k separably closed), and one sentence at each use. |
| `thm:picard-rr` proof (~2588) | The induction shows only D→D−x. The n_x<0 case (via D+x) and H^{≥2}=0 are left implicit. | One sentence each. |
| `prop:av-rigidity` (~1302) | The counterexample (ℂ/ℝ) shows only that geometric *connectedness* is needed. Spec ℂ is geometrically reduced. | Add a second example: k imperfect, X=Spec k(a^{1/p}), Y=𝔸¹_k, Z=X×Y, f=id. Or reword. |
| Abelian reference tables (~844, ~1974, ~1975) | They still credit `prop:av-const-locus` to 0AH8 (now 01UA) and rigidity Step 4 to Milne/Mumford (now proved via 0BUG). | Update the rows. |
| `prop:av-const-locus` | Edge case X=∅: "y∈L iff …" fails, though the conclusion holds. | Add "X nonempty". |
| `thm:sf-kunneth-verdier` α step (~8592) | Open localization is skipped. Rf^! does not commute with j_!. The route via Rj_* leaves i^*Rj_*F on the boundary, which needs an induction on the dimension of the support. `lem:sf-kunneth-star` is not cited. The conclusion is true. | Spell out the induction. |
| `thm:sf-kunneth-relative` (i), (iii) | Symmetry and base-change coherence need PF to be compatible with Ex_!. No cited node states that. True (SGA 4 XVII), but it is a missing input. | State or cite it. |
| `thm:sf-kunneth-relative` step (4) (~8197) | Forward reference to `thm:sf-ctf-stability` (needed for Rf_!K ∈ D_ctf, also by the typing of PF). | Renumber or reorder (no cycle). |
| `lem:sf-ctf-generation` proof | It "runs the proof of" `lem:sf-flat-model`, which as stated gives only flat sheaves, not flat *constructible* ones. The key input (constructible sheaves are quotients of ⊕ j_{V!}Λ_V, Stacks 095M) is not stated. | State the constructible variant, or cite it. |
| `d:real-weil`, `d:real-boundary` | Correct. The conjugacy claims omit the one-line reason Ẑ = ℤ + e_xẐ ⇒ g = w·Frob_x^t with w ∈ W. | Add the sentence. |
| `prop:an` Note (~6630) | Says the Rz^! form is "never used later". `thm:regular` and `cor:trace` now use it. | Delete the note. |
| `thm:regular`(b) | The "pur_s for 𝔸¹_Y" clause is inside the theorem only for Y smooth over k. | Qualify. |
| `lem:finite` | The new example "F₂[−1]" needs ℓ=2. | Write Λ[−1]. |

## 3. Problems that predate today (not from the audit)

Ordered roughly by severity. For each: confidence, and whether anything downstream breaks.

1. **`thm:intfactors` (ii), ~15331, false step.** Frobenius preserving H^i(X,ℤ_ℓ) gives only ℓ-integrality (ℤ_(ℓ), or ℤ[1/p] over all ℓ), not P_i ∈ ℤ[T]. "Z = A/B with A,B ∈ ℤ[T]" also needs Fatou's lemma, which is never stated. Fix: Fatou + P_i | A or B in ℚ[T] + Gauss's lemma. The integrality of the Frobenius factors depends on it.
2. **`thm:picard-perfect`, ~2470, false statement.** "On the locus where rank ≤ r the restriction is flat of rank r". Counterexample: f=id, F=O, r=5. It should say: finite locally free of locally constant rank ≤ r. The open conditions should be on the fibre cohomology.
3. **`thm:p1` proof (i), ~4492, false statement.** It claims H^q(C,F_r)=0 for q≥2 and "étale cd of a curve is 1". For a proper curve, H²(C,μ_r)=ℤ/r. The bound 1 holds only for affine curves. "The analogues hold for F_p": H¹(C,F_p) has dimension equal to the p-rank (≤ g), not 2g.
4. **`thm:curveestimate`, false for 0-dimensional C.** `def:curve` allows dimension ≤ 1. For C = Spec k, H²(C,ℤ/n)=0. `def:pic`(P2) (deg surjective) also fails. Fix: require dimension 1.
5. **`input:weights` relative form, ~15049, false as worded.** "Rf_! carries weights ≤ w to ≤ w + (relative dimension)". 𝔸¹→pt: H²_c has weight 2 > 1. It should be "R^rf_! has weights ≤ w+r" or "Rf_!K has weights ≤ w".
6. **`prop:nagata-sketch-zmt`(ii), ~231.** False if "quasi-affine S-scheme" is read relatively. Counterexample: S=ℙ¹, X = Spec_S Sym O(−1). Stacks 04II needs X quasi-affine as a scheme. Uses only need an affine base. Fix the wording.
7. **`prop:normal-form` proof, ~5038.** The slicing step needs κ(x)/κ(s) separable. Counterexample: S = Spec F_p(t), x: u^p=t. "Miracle flatness" (~5027) is applied over a non-regular base, though the conclusion is true.
8. **`thm:picard-serre-b` / `-a` proofs, ~2372.** "A hypersurface Z *containing* X": the exact sequence is wrong. It needs a hypersurface avoiding the associated points. It cites nonexistent "(ii)", "(iii)" of `thm:picard-pn`.
9. **`i:real-boundary` proof Step 2, ~12730.** It writes I_s = Gal(K̄_s/K_s) with K_s henselian. That is the decomposition group. Inertia is Gal(K̄_s/K_s^{sh}). It contradicts `d:real-boundary`.
10. **`thm:betti`, ~15511.** "Pole of order 1 at T=1 and at q^{−d}" is read off without excluding cancellation. It needs weight separation (`prop:separation`/`prop:rootpurity`), which is not cited.
11. **`prop:stalk` (P3) proof, ~13346.** It says "smooth base change" where it should be proper/compact-support base change (`prop:sf-cbc`). The kernel should be L_ψ(⟨x,ξ_univ⟩).
12. **`thm:sf-direct-image-tor-amplitude` proof, ~8256.** It cites the compact-support projection formula `rem:sf-pf-done` for Rf_* with f not proper. The identity is true by a way-out argument.
13. **`lem:finite` Step 3, ~10459.** Perfectness of ordinary RΓ is claimed at the O_E/E/Q̄_ℓ stages but argued only for RΓ_c.
14. **`def:ops`, ~10301.** "Rf^! ⊣ Rf_!" has the adjunction backwards.
15. **Smaller:**
    - `prop:av-mult-finite` and `thm:av-final`(b) cite algebraically-closed lemmas over any k. "Reduced ⇒ étale" for finite schemes over an imperfect field is false; base change to k̄ fixes it.
    - `prop:av-symmetric-ample`: Segre should be applied to L and [−1]*L.
    - `thm:vanishing` (q=1): a torsor is not a connected Galois cover.
    - `lem:failure-field`: needs T qcqs as a scheme (reduce to affine S).
    - `thm:picard-semicon`: "coherent" → "finitely presented" over a non-Noetherian base.
    - `def:fourier-set`: needs μ_p ⊂ E for 𝒦_ψ to be an E-sheaf.
    - `def:purity-conv`: N is undefined; the torsor exponent should be T^{ℓ^N}.
    - `thm:fe` proof: the exponent sign is −χ in an intermediate step.
    - `def:sf-kv-maps`(iii): E_i is undeclared.
    - Garbled sentences in `p:frob` (~9648) and `prop:rootpurity` (~15250).
    - `r:linear-library` is cited for a criterion it doesn't contain.
    - `prop:br-inj`: "finitely many closures" justification.
    - `rem:picard-zero` remark: missing pr_T^*.
    - `def:cohfamily`/`def:roots` forward-reference `thm:intfactors` in text.
