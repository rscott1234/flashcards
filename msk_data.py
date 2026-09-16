MSK_JOINTS = [
    {"key": "shoulder", "label": "Shoulder"},
    {"key": "elbow", "label": "Elbow"},
    {"key": "wrist-hand", "label": "Wrist & Hand"},
    {"key": "cervical", "label": "Cervical Spine"},
    {"key": "lumbar", "label": "Lumbar Spine & SIJ"},
    {"key": "hip", "label": "Hip"},
    {"key": "knee", "label": "Knee"},
    {"key": "ankle-foot", "label": "Ankle & Foot"},
]

MSK_SPECIAL_TESTS = {
    "shoulder": {
        "label": "Shoulder",
        "description": "The glenohumeral joint is the most mobile joint in the body, relying on a complex interplay of static (ligamentous) and dynamic (rotator cuff, scapular stabilisers) restraints. Special tests help differentiate between impingement, rotator cuff pathology, instability, labral tears, and AC joint pathology.",
        "tests": [
            {
                "name": "Neer's Test",
                "image": "neers-test.jpg",
                "purpose": "Detect subacromial impingement (supraspinatus tendon, biceps tendon, subacromial bursa)",
                "procedure": "The examiner stabilises the scapula with one hand and passively elevates the patient's arm in forced forward flexion (sagittal plane). No rotation is applied.",
                "positive_sign": "Pain reported in the anterolateral shoulder (deltoid region) between 60-120 degrees of elevation. Patient's facial expression or voice response is noted.",
                "sensitivity": 0.78,
                "specificity": 0.58,
                "lr_positive": 1.9,
                "lr_negative": 0.38,
                "notes": "More of a sensitivity test — a negative result helps rule out impingement, but a positive result isn't highly specific. The test compresses the supraspinatus tendon against the anteroinferior acromion."
            },
            {
                "name": "Hawkins-Kennedy Test",
                "image": "hawkins-kennedy-test.jpg",
                "purpose": "Detect subacromial impingement (supraspinatus tendon impinged against the coracoacromial ligament)",
                "procedure": "The examiner flexes the patient's shoulder and elbow to 90 degrees, then forcibly internally rotates the shoulder. This drives the greater tuberosity under the coracoacromial arch.",
                "positive_sign": "Pain reported in the shoulder during internal rotation. The patient may lean forward or attempt to stop the movement.",
                "sensitivity": 0.79,
                "specificity": 0.59,
                "lr_positive": 1.9,
                "lr_negative": 0.36,
                "notes": "Similar to Neer's — good sensitivity, moderate specificity. Often used as a screening test in combination with other impingement signs."
            },
            {
                "name": "Empty Can Test (Jobe's Test)",
                "image": "empty-can-test.jpg",
                "purpose": "Assess supraspinatus tendon integrity (tendinopathy or tear)",
                "procedure": "Patient's shoulder is abducted to 90 degrees in the scapular plane (30 degrees forward from the coronal plane) and fully internally rotated so the thumb points downward ('emptying a can'). The examiner applies downward resistance.",
                "positive_sign": "Pain and/or weakness with resisted elevation. Pain suggests tendinopathy; significant weakness suggests a tear.",
                "sensitivity": 0.89,
                "specificity": 0.50,
                "lr_positive": 1.8,
                "lr_negative": 0.22,
                "notes": "High sensitivity — useful for ruling out supraspinatus pathology when negative. The scapular plane position optimises tension on the supraspinatus. Also called Jobe's test."
            },
            {
                "name": "Full Can Test",
                "image": "full-can-test.jpg",
                "purpose": "Assess supraspinatus strength (alternative to Empty Can, less painful)",
                "procedure": "Patient's shoulder is abducted to 90 degrees in the scapular plane, but with the forearm supinated and thumb pointing upward ('holding a can'). The examiner applies downward resistance.",
                "positive_sign": "Weakness compared to the unaffected side. Less painful than the Empty Can test while still loading the supraspinatus.",
                "sensitivity": 0.64,
                "specificity": 0.63,
                "lr_positive": 1.7,
                "lr_negative": 0.57,
                "notes": "Less provocative than the Empty Can test. Preferred when the Empty Can is too painful, but has lower sensitivity."
            },
            {
                "name": "Drop Arm Test",
                "image": "drop-arm-test.jpg",
                "purpose": "Detect a full-thickness supraspinatus tear (inability to actively control arm lowering)",
                "procedure": "The examiner passively abducts the patient's arm to 90 degrees (or fully overhead) and asks the patient to slowly lower the arm back to the side.",
                "positive_sign": "The patient is unable to control the descent — the arm drops suddenly (positive) or the patient cannot maintain the abducted position. Pain alone is not a positive test.",
                "sensitivity": 0.27,
                "specificity": 0.88,
                "lr_positive": 2.3,
                "lr_negative": 0.83,
                "notes": "High specificity but very low sensitivity — a positive result strongly suggests a full-thickness tear (rule in), but a negative result does NOT rule out a tear. Not useful as a screening test."
            },
            {
                "name": "External Rotation Lag Sign",
                "image": "external-rotation-lag-sign.jpg",
                "purpose": "Detect infraspinatus/teres minor tear (posterior rotator cuff)",
                "procedure": "With the patient seated, the examiner passively flexes the elbow to 90 degrees and brings the shoulder into 20 degrees of abduction and near-full external rotation (elbow supported). The patient is asked to actively maintain this position as the examiner releases the wrist.",
                "positive_sign": "A 'lag' or drop-back of the forearm toward internal rotation, indicating the patient cannot maintain the externally rotated position against gravity.",
                "sensitivity": 0.70,
                "specificity": 0.96,
                "lr_positive": 17.5,
                "lr_negative": 0.31,
                "notes": "Highly specific for a full-thickness infraspinatus tear. A lag indicates at least a moderate tear involving the posterior cuff."
            },
            {
                "name": "Lift-Off Test (Gerber's Test)",
                "image": "lift-off-test.jpg",
                "purpose": "Assess subscapularis tendon integrity (internal rotator)",
                "procedure": "The patient places the dorsum of the hand against the mid-lumbar spine (hand behind back). The examiner asks the patient to actively lift the hand away from the back (internal rotation). Resistance can be applied.",
                "positive_sign": "Inability to lift the hand off the back, or significant weakness compared to the unaffected side. The patient may 'cheat' by extending the elbow or trunk.",
                "sensitivity": 0.42,
                "specificity": 0.97,
                "lr_positive": 14.0,
                "lr_negative": 0.60,
                "notes": "Very specific for subscapularis tear — a positive result is highly indicative, but a negative result does NOT rule out subscapularis pathology. Many patients with intact subscapularis cannot perform this movement due to stiffness."
            },
            {
                "name": "Apprehension Test (Crank Test)",
                "image": "apprehension-test.jpg",
                "purpose": "Assess anterior glenohumeral instability",
                "procedure": "Patient lies supine. The examiner abducts the shoulder to 90 degrees and slowly externally rotates, applying a gentle anteriorly directed force to the humeral head.",
                "positive_sign": "The patient demonstrates apprehension (facial expression of fear, muscle guarding) or reports a sensation that the shoulder is 'about to pop out'. Pain alone is not considered a true positive.",
                "sensitivity": 0.68,
                "specificity": 0.78,
                "lr_positive": 3.1,
                "lr_negative": 0.41,
                "notes": "Distinguish between apprehension (positive test) and pain (which may indicate impingement). Always compare bilaterally. The relocation test can be used as a follow-up."
            },
            {
                "name": "Relocation Test (Jobe's Relocation)",
                "image": "relocation-test.jpg",
                "purpose": "Confirm anterior instability (follow-up to Apprehension Test)",
                "procedure": "Performed immediately after a positive Apprehension Test. While maintaining the shoulder in the apprehensive position (90 deg abduction, external rotation), the examiner applies a posteriorly directed force to the anterior humeral head.",
                "positive_sign": "Reduction or elimination of the patient's apprehension (not just pain relief). The patient feels 'safer' and may allow further external rotation.",
                "sensitivity": 0.57,
                "specificity": 0.87,
                "lr_positive": 4.4,
                "lr_negative": 0.49,
                "notes": "A positive relocation test significantly increases the likelihood of anterior instability. Often used together with the Apprehension Test and the Surprise/Release Test."
            },
            {
                "name": "Anterior Drawer Test (Shoulder)",
                "image": "anterior-drawer-shoulder.jpg",
                "purpose": "Assess anterior glenohumeral laxity",
                "procedure": "Patient supine with arm at 80-100 degrees abduction, 0-20 degrees forward flexion, 0-30 degrees external rotation. The examiner grasps the proximal humerus with one hand and stabilises the scapula with the other, translating the humeral head anteriorly.",
                "positive_sign": "Excessive anterior translation of the humeral head relative to the glenoid fossa compared to the unaffected side. A clunk or reproduction of symptoms may also be noted.",
                "sensitivity": 0.53,
                "specificity": 0.84,
                "lr_positive": 3.3,
                "lr_negative": 0.56,
                "notes": "Requires practice to perform reliably. Always compare to the contralateral side as some individuals have generalised laxity."
            },
            {
                "name": "O'Brien's Test (Active Compression Test)",
                "image": "obriens-test.jpg",
                "purpose": "Differentiate between SLAP lesion and AC joint pathology",
                "procedure": "Patient standing, arm forward flexed to 90 degrees, adducted 10-15 degrees across the midline, fully internally rotated (thumb down). The examiner applies downward force. The test is repeated with the forearm fully supinated (palm up).",
                "positive_sign": "Pain in the first position (internal rotation, thumb down) that is reduced or eliminated in the second position (supinated, palm up). Pain 'on top' of the shoulder suggests AC joint; pain 'inside' the shoulder suggests a SLAP lesion.",
                "sensitivity": 0.68,
                "specificity": 0.81,
                "lr_positive": 3.6,
                "lr_negative": 0.40,
                "notes": "The location of pain helps differentiate between SLAP (deep, posterior) and AC joint (superior). Often positive in both conditions, so use with other tests."
            },
            {
                "name": "AC Joint Shear (Cross-Body Adduction) Test",
                "image": "ac-joint-shear-test.jpg",
                "purpose": "Assess AC joint pathology",
                "procedure": "The examiner passively flexes the patient's shoulder to 90 degrees and adducts the arm horizontally across the chest toward the opposite shoulder.",
                "positive_sign": "Pain localised directly over the AC joint (point tenderness). The patient may wince or protect the joint.",
                "sensitivity": 0.77,
                "specificity": 0.73,
                "lr_positive": 2.9,
                "lr_negative": 0.32,
                "notes": "Simple and quick test. AC joint pain can be confirmed by injecting local anaesthetic into the joint (pain relief confirms the diagnosis)."
            },
        ]
    },
    "elbow": {
        "label": "Elbow",
        "description": "The elbow is a hinge joint (humeroulnar) with rotational components (radioulnar). Common pathologies include lateral epicondylalgia (tennis elbow), medial epicondylalgia (golfer's elbow), ligamentous injuries (particularly UCL), and osteochondritis dissecans.",
        "tests": [
            {
                "name": "Cozen's Test (Resisted Wrist Extension)",
                "image": "cozens-test.jpg",
                "purpose": "Detect lateral epicondylalgia (tennis elbow) — extensor carpi radialis brevis tendinopathy",
                "procedure": "The patient's forearm is supported (elbow flexed to 90 degrees, forearm pronated). The examiner stabilises the elbow with one hand and asks the patient to actively extend the wrist against resistance while the examiner palpates the lateral epicondyle.",
                "positive_sign": "Sharp pain reproduced at the lateral epicondyle (origin of ECRB) during resisted wrist extension. Pain may radiate down the extensor forearm.",
                "sensitivity": None,
                "specificity": None,
                "lr_positive": None,
                "lr_negative": None,
                "notes": "Highly specific for lateral epicondylalgia when pain is localised to the lateral epicondyle. Maudsley's test is a similar alternative using resisted middle finger extension."
            },
            {
                "name": "Mill's Test",
                "image": "mills-test.jpg",
                "purpose": "Detect lateral epicondylalgia (tennis elbow) — stretching the extensor mechanism",
                "procedure": "The examiner passively extends the patient's elbow with the forearm pronated and wrist fully flexed. This stretches the extensor muscles at their origin on the lateral epicondyle.",
                "positive_sign": "Pain reproduced at the lateral epicondyle during the stretch. The patient may feel a pulling sensation along the extensor forearm.",
                "sensitivity": 0.53,
                "specificity": 1.00,
                "lr_positive": None,
                "lr_negative": 0.47,
                "notes": "High specificity — a positive test strongly suggests lateral epicondylalgia. Less sensitive than Cozen's test. More useful as a confirmatory than a screening test."
            },
            {
                "name": "Medial Epicondylalgia Test (Reverse Cozen's / Golfer's Elbow Test)",
                "image": "medial-epicondylalgia-test.jpg",
                "purpose": "Detect medial epicondylalgia (golfer's elbow) — flexor/pronator tendinopathy",
                "procedure": "The examiner stabilises the patient's elbow at 90 degrees with the forearm supinated. The patient resists wrist pronation and/or wrist flexion as the examiner applies force. The examiner may palpate the medial epicondyle.",
                "positive_sign": "Pain reproduced at the medial epicondyle during resisted pronation or wrist flexion. The flexor origin is stressed.",
                "sensitivity": None,
                "specificity": None,
                "lr_positive": None,
                "lr_negative": None,
                "notes": "Less common than lateral epicondylalgia but follows the same clinical reasoning. Resisted pronation tends to be more provocative than resisted wrist flexion."
            },
            {
                "name": "Valgus Stress Test (Elbow)",
                "image": "valgus-stress-elbow.jpg",
                "purpose": "Assess ulnar collateral ligament (UCL) integrity at the medial elbow",
                "procedure": "The patient's elbow is flexed to 20-30 degrees (to unlock the olecranon from the fossa). The examiner applies a valgus (abduction) force to the elbow while stabilising the distal humerus medially.",
                "positive_sign": "Excessive medial joint line gapping, a soft end-feel, or reproduction of pain/instability. Compare to the unaffected side.",
                "sensitivity": 0.69,
                "specificity": 0.81,
                "lr_positive": 3.6,
                "lr_negative": 0.38,
                "notes": "The UCL is the primary stabiliser against valgus stress. Common in throwing athletes (e.g. baseball pitchers). Test at both 20-30 degrees (UCL) and full extension (general laxity)."
            },
            {
                "name": "Varus Stress Test (Elbow)",
                "image": "varus-stress-elbow.jpg",
                "purpose": "Assess lateral collateral ligament (LCL) integrity at the lateral elbow",
                "procedure": "The patient's elbow is flexed to 20-30 degrees. The examiner applies a varus (adduction) force to the elbow while stabilising the distal humerus laterally.",
                "positive_sign": "Excessive lateral joint line gapping, a soft end-feel, or reproduction of pain/instability on the lateral side. Compare to the unaffected side.",
                "sensitivity": None,
                "specificity": None,
                "lr_positive": None,
                "lr_negative": None,
                "notes": "LCL injuries are less common than UCL injuries. The LCL complex includes the radial collateral ligament, annular ligament, and lateral ulnar collateral ligament (LUCL)."
            },
            {
                "name": "Tinel's Sign (Elbow/Cubital Tunnel)",
                "image": "tinels-elbow.jpg",
                "purpose": "Detect ulnar nerve irritation at the cubital tunnel (behind the medial epicondyle)",
                "procedure": "The examiner taps (percusses) firmly over the ulnar nerve at the cubital tunnel (posterior to the medial epicondyle) 4-6 times.",
                "positive_sign": "Reproduction of tingling, pins-and-needles, or electric shock sensation radiating into the ring and little fingers (ulnar nerve distribution).",
                "sensitivity": 0.66,
                "specificity": 0.76,
                "lr_positive": 2.8,
                "lr_negative": 0.45,
                "notes": "Also test at the Guyon's canal (wrist) for distal ulnar nerve entrapment. Ulnar nerve compression at the elbow is the second most common entrapment neuropathy (after carpal tunnel)."
            },
        ]
    },
    "wrist-hand": {
        "label": "Wrist & Hand",
        "description": "The wrist and hand complex involves multiple small joints, tendons, and nerves. Common conditions include carpal tunnel syndrome, De Quervain's tenosynovitis, TFCC injuries, scaphoid fractures, and various ligamentous instabilities.",
        "tests": [
            {
                "name": "Phalen's Test (Wrist Flexion)",
                "image": "phalens-test.jpg",
                "purpose": "Detect median nerve compression at the carpal tunnel",
                "procedure": "The patient is asked to hold both wrists in full, unforced flexion (pressing the dorsums of the hands together) for 30-60 seconds. The examiner can also passively flex the patient's wrists.",
                "positive_sign": "Reproduction of tingling, numbness, or paraesthesia in the median nerve distribution (thumb, index, middle, and half of ring finger) within 60 seconds.",
                "sensitivity": 0.68,
                "specificity": 0.73,
                "lr_positive": 2.5,
                "lr_negative": 0.44,
                "notes": "The most commonly used provocative test for carpal tunnel syndrome. More sensitive but less specific than Tinel's sign at the wrist. Reverse Phalen's (extension) can also be used."
            },
            {
                "name": "Tinel's Sign (Wrist/Carpal Tunnel)",
                "image": "tinels-wrist.jpg",
                "purpose": "Detect median nerve irritation at the carpal tunnel",
                "procedure": "The examiner taps (percusses) firmly over the median nerve at the wrist (between the palmaris longus and flexor carpi radialis tendons, just proximal to the wrist crease) 4-6 times.",
                "positive_sign": "Reproduction of tingling or electric shock sensation radiating into the thumb, index, and middle fingers (median nerve distribution).",
                "sensitivity": 0.50,
                "specificity": 0.77,
                "lr_positive": 2.2,
                "lr_negative": 0.65,
                "notes": "Less sensitive than Phalen's but more specific. A negative Tinel's does NOT rule out carpal tunnel syndrome. A 'positive Tinel's' should reproduce symptoms along the nerve distribution, not just local tenderness."
            },
            {
                "name": "Carpal Compression Test (Durkan's Test)",
                "image": "carpal-compression-test.jpg",
                "purpose": "Detect carpal tunnel syndrome by direct median nerve compression",
                "procedure": "The examiner applies firm direct pressure (using thumbs) over the carpal tunnel at the proximal wrist crease for 30 seconds.",
                "positive_sign": "Reproduction of tingling or numbness in the median nerve distribution (thumb, index, middle fingers) within 30 seconds.",
                "sensitivity": 0.87,
                "specificity": 0.90,
                "lr_positive": 8.7,
                "lr_negative": 0.14,
                "notes": "Higher diagnostic accuracy than Phalen's and Tinel's. A positive test significantly increases the likelihood of carpal tunnel syndrome."
            },
            {
                "name": "Finkelstein's Test",
                "image": "finkelsteins-test.jpg",
                "purpose": "Detect De Quervain's tenosynovitis (stenosing tenosynovitis of the first dorsal compartment — APL and EPB tendons)",
                "procedure": "The patient makes a fist with the thumb tucked inside the fingers. The examiner then passively deviates the wrist in an ulnar direction (toward the little finger).",
                "positive_sign": "Sharp pain reproduced over the radial styloid (first dorsal compartment tendons). The patient may report a 'catching' or 'snapping' sensation.",
                "sensitivity": 0.89,
                "specificity": 0.89,
                "lr_positive": 8.1,
                "lr_negative": 0.12,
                "notes": "Also called Eichhoff's test. High diagnostic accuracy. A variation (Brunelli's test) asks the patient to actively extend the thumb against resistance for a more specific load."
            },
            {
                "name": "Watson's Test (Scaphoid Shift Test)",
                "image": "watsons-test.jpg",
                "purpose": "Assess scapholunate instability (scapholunate dissociation)",
                "procedure": "The examiner applies thumb pressure to the distal pole of the scaphoid from the palmar aspect while moving the wrist from ulnar deviation into radial deviation. The scaphoid is normally vertical in ulnar deviation and horizontal in radial deviation.",
                "positive_sign": "A painful clunk or shift as the scaphoid subluxes dorsally out of the scaphoid fossa, followed by a snap when pressure is released. The patient may report a sense of instability.",
                "sensitivity": 0.69,
                "specificity": 0.68,
                "lr_positive": 2.2,
                "lr_negative": 0.46,
                "notes": "Requires practice and 'feel' for the normal scaphoid movement. Compare bilaterally. Positive test suggests scapholunate interosseous ligament injury."
            },
            {
                "name": "TFCC Load Test (Ulnar Grind / Ulnocarpal Stress Test)",
                "image": "tfcc-load-test.jpg",
                "purpose": "Detect Triangular Fibrocartilage Complex (TFCC) pathology on the ulnar side of the wrist",
                "procedure": "The examiner axially loads the wrist in ulnar deviation while rotating the forearm, compressing the TFCC between the ulnar head and the carpal bones.",
                "positive_sign": "Pain or a clicking/grinding sensation over the ulnar aspect of the wrist (between the ulnar styloid and triquetrum).",
                "sensitivity": None,
                "specificity": None,
                "lr_positive": None,
                "lr_negative": None,
                "notes": "TFCC injuries are common after a fall on an outstretched hand. MR arthrography is the gold standard for imaging. The piano key test assesses distal radioulnar joint instability."
            },
        ]
    },
    "cervical": {
        "label": "Cervical Spine",
        "description": "The cervical spine supports the head, protects the spinal cord, and allows a large range of motion. Common pathologies include disc herniation, cervical radiculopathy, facet joint dysfunction, whiplash-associated disorders, and myelopathy.",
        "tests": [
            {
                "name": "Spurling's Test (Cervical Compression / Foraminal Compression)",
                "image": "spurlings-test.jpg",
                "purpose": "Detect cervical nerve root compression/irritation (cervical radiculopathy)",
                "procedure": "The patient's head is placed in extension and lateral flexion toward the symptomatic side. The examiner applies gentle downward axial compression through the top of the head (approximately 7-10 kg of force).",
                "positive_sign": "Reproduction of the patient's radicular symptoms (pain, tingling, numbness, or electric shock) radiating into the ipsilateral upper limb. Local neck pain alone is NOT a positive test.",
                "sensitivity": 0.50,
                "specificity": 0.87,
                "lr_positive": 3.8,
                "lr_negative": 0.57,
                "notes": "High specificity — a positive test is highly suggestive of cervical radiculopathy. Always screen for vertebrobasilar insufficiency (VBI) and red flags before performing. Do not perform in acute trauma or known instability."
            },
            {
                "name": "Distraction Test (Cervical Axial Distraction / Decompression)",
                "image": "distraction-test.jpg",
                "purpose": "Assess whether cervical nerve root compression is the source of upper limb symptoms",
                "procedure": "The examiner grasps the patient's head under the occiput and chin and applies a gentle upward/distraction force, lifting the head to unload the cervical spine (approximately 10-15 kg of lift).",
                "positive_sign": "Relief or reduction of the patient's radicular symptoms (pain, tingling) in the upper limb. This is a positive distraction test.",
                "sensitivity": 0.44,
                "specificity": 0.90,
                "lr_positive": 4.4,
                "lr_negative": 0.62,
                "notes": "High specificity — a positive test (symptom relief) strongly suggests cervical radiculopathy. Inexpensive and safe. Distraction opens the intervertebral foramen and reduces pressure on the nerve root."
            },
            {
                "name": "Upper Limb Tension Test (ULTT) — Median Nerve Bias",
                "image": "ultt-median.jpg",
                "purpose": "Assess mechanosensitivity of the median nerve and brachial plexus (neurodynamic testing)",
                "procedure": "The patient lies supine. The examiner sequentially: (1) depresses the shoulder girdle, (2) abducts the arm to 90-110 degrees, (3) supinates the forearm, (4) extends the wrist and fingers, (5) extends the elbow, (6) adds contralateral cervical side flexion (sensitising manoeuvre).",
                "positive_sign": "Reproduction of the patient's symptoms (stretch, tingling, or pain) along the upper limb, with symptom reduction when the neck is side-flexed toward the tested side (reduces tension on the nerve).",
                "sensitivity": 0.83,
                "specificity": 0.65,
                "lr_positive": 2.4,
                "lr_negative": 0.26,
                "notes": "Good sensitivity for detecting neural mechanosensitivity. Three main biases: Median (ULTT1), Radial (ULTT2a), and Ulnar (ULTT2b). Always compare to the unaffected limb. The sensitising manoeuvre (contralateral neck flexion) is critical for confirming neural rather than muscular restriction."
            },
            {
                "name": "Sharp-Purser Test",
                "image": "sharp-purser-test.jpg",
                "purpose": "Assess atlantoaxial instability (transverse ligament laxity)",
                "procedure": "The patient's head is in slight flexion. The examiner places one hand on the patient's forehead and the other hand on the spinous process of C2 (axis). An anterior-to-posterior force is applied to the forehead while the C2 spinous process is stabilised posteriorly.",
                "positive_sign": "A subjective 'clunk' or sensation of the head sliding forward (C1 translating anteriorly on C2), or reproduction of the patient's symptoms (dizziness, visual changes, or neurological symptoms).",
                "sensitivity": 0.69,
                "specificity": 0.96,
                "lr_positive": 17.3,
                "lr_negative": 0.32,
                "notes": "VERY HIGH SPECIFICITY — a positive test strongly suggests atlantoaxial instability. This is a potentially dangerous test. ONLY perform if there is clinical suspicion of instability (e.g. rheumatoid arthritis, Down syndrome, trauma). Contraindicated in acute cervical fracture or known instability."
            },
            {
                "name": "Vertebrobasilar Insufficiency (VBI) Test",
                "image": "vbi-test.jpg",
                "purpose": "Screen for vertebrobasilar artery insufficiency before high-velocity cervical manipulation",
                "procedure": "The patient is supine with the head extending over the edge of the plinth. The examiner passively positions the patient's head in extension, rotation, and lateral flexion (sequential or combined). Hold each position for 30-45 seconds.",
                "positive_sign": "Provocation of pre-syncopal symptoms: dizziness, nystagmus, visual disturbances (blurring, double vision), dysarthria, dysphagia, nausea, drop attack, or altered consciousness.",
                "sensitivity": None,
                "specificity": None,
                "lr_positive": None,
                "lr_negative": None,
                "notes": "No validated sensitivity/specificity data exists. This is a screening test with medicolegal importance. A negative test does NOT guarantee safety of manipulation. Always document results. Stop immediately if ANY positive sign appears."
            },
        ]
    },
    "lumbar": {
        "label": "Lumbar Spine & SIJ",
        "description": "The lumbar spine bears significant load and allows flexion, extension, and rotation. The sacroiliac joint (SIJ) connects the spine to the pelvis. Common lumbar pathologies include disc herniation, spinal stenosis, facet joint dysfunction, and SIJ dysfunction.",
        "tests": [
            {
                "name": "Straight Leg Raise (SLR / Lasègue's Test)",
                "image": "slr-test.jpg",
                "purpose": "Detect lumbar nerve root irritation (L4-S1), particularly disc herniation causing lower lumbar radiculopathy",
                "procedure": "The patient lies supine. The examiner passively lifts the patient's symptomatic leg with the knee fully extended, while maintaining the ankle in neutral dorsiflexion (this adds tension to the sciatic nerve and nerve roots).",
                "positive_sign": "Reproduction of the patient's radicular symptoms (pain, tingling, electric shock) radiating below the knee into the leg/foot, typically between 30-70 degrees of hip flexion. Above 70 degrees, the movement stresses the contralateral SIJ and hamstrings rather than nerve roots.",
                "sensitivity": 0.85,
                "specificity": 0.49,
                "lr_positive": 1.7,
                "lr_negative": 0.31,
                "notes": "Good sensitivity, poor specificity. A negative SLR below 70 degrees significantly reduces the likelihood of disc herniation (good for ruling out). Dorsiflexion of the ankle (Braggard's test) can be added as a sensitising manoeuvre. The crossed SLR (pain in the symptomatic leg when the unaffected leg is lifted) is highly specific but less sensitive."
            },
            {
                "name": "Femoral Nerve Stretch Test (Prone Knee Bend / Reverse SLR)",
                "image": "femoral-nerve-stretch.jpg",
                "purpose": "Detect upper lumbar nerve root irritation (L2-L4, femoral nerve)",
                "procedure": "The patient lies prone. The examiner passively flexes the patient's knee toward the buttock (bringing the heel toward the gluteal region), extending the hip. This stretches the femoral nerve (L2-L4 nerve roots).",
                "positive_sign": "Reproduction of anterior thigh pain/tingling (femoral nerve distribution) or groin pain. The patient may spontaneously lift the pelvis off the bed to reduce tension.",
                "sensitivity": None,
                "specificity": None,
                "lr_positive": None,
                "lr_negative": None,
                "notes": "Useful when upper lumbar nerve root involvement is suspected (e.g. L2/L3/L4 disc herniation, which is much less common than L4/L5 or L5/S1). Also called the Prone Knee Bend Test."
            },
            {
                "name": "Slump Test",
                "image": "slump-test.jpg",
                "purpose": "Assess mechanosensitivity of the spinal cord, dura mater, and nerve roots (neurodynamic test for the entire neuraxis)",
                "procedure": "The patient sits on the edge of the plinth. The examiner sequentially: (1) asks the patient to 'slump' (thoracolumbar flexion), (2) applies overpressure to the cervical spine (neck flexion), (3) asks the patient to actively extend one knee, (4) adds ankle dorsiflexion. The cervical component is then released as a sensitising manoeuvre.",
                "positive_sign": "Reproduction of the patient's symptoms (posterior leg/back pain, stretch, or tingling) that reduces when the neck is extended (reducing tension on the neuraxis).",
                "sensitivity": 0.84,
                "specificity": 0.83,
                "lr_positive": 4.9,
                "lr_negative": 0.19,
                "notes": "Good diagnostic accuracy for lumbar nerve root compression. The key clinical sign is symptom modification with neck movement (flexion increases symptoms, extension reduces them — confirming neural mechanosensitivity)."
            },
            {
                "name": "Lumbar Quadrant Test (Extension-Rotation Test / Kemp's Test)",
                "image": "lumbar-quadrant-test.jpg",
                "purpose": "Detect lumbar facet joint pathology or foraminal stenosis (provocative test)",
                "procedure": "The patient stands. The examiner supports the patient and passively moves them into combined extension, lateral flexion, and rotation toward the symptomatic side (the 'quadrant' or closing position).",
                "positive_sign": "Reproduction of localised lumbar pain (suggests facet joint) or radicular pain into the leg (suggests foraminal stenosis). Extension-rotation to the opposite side opens the foramen.",
                "sensitivity": None,
                "specificity": None,
                "lr_positive": None,
                "lr_negative": None,
                "notes": "Poor diagnostic accuracy in isolation. Used as part of a clinical cluster for lumbar facet joint pain. When combined with other findings (centralisation, age, extension pain), it is more useful."
            },
            {
                "name": "SIJ Cluster Tests (4-Test Cluster)",
                "image": "sij-cluster.jpg",
                "purpose": "Identify sacroiliac joint (SIJ) dysfunction as the source of posterior pelvic/low back pain",
                "procedure": "Four tests are performed: (1) Distraction/Gapping Test — pressure applied to bilateral ASIS to 'gap' the SIJ, (2) Compression/Thigh Squeeze Test — side-lying pressure on the iliac crest, (3) Thigh Thrust (Posterior Shear) Test — supine, hip 90 deg, axial load through femur posteriorly, (4) Gaenslen's Test — supine, one hip flexed maximally, the other extended off the edge of the plinth.",
                "positive_sign": "3 or more positive tests out of 4 suggests SIJ dysfunction (pain provocation in the SIJ region, typically inferior to the PSIS, buttock, or groin).",
                "sensitivity": 0.85,
                "specificity": 0.87,
                "lr_positive": 6.5,
                "lr_negative": 0.17,
                "notes": "No single SIJ provocation test is diagnostic in isolation. The 4-test cluster (3/4 positive) significantly increases the likelihood of SIJ pain. SIJ pain is notoriously difficult to diagnose and is often confused with lumbar pathology."
            },
        ]
    },
    "hip": {
        "label": "Hip",
        "description": "The hip is a large weight-bearing ball-and-socket joint. Common pathologies include osteoarthritis, femoroacetabular impingement (FAI), labral tears, gluteal tendinopathy, and hip flexor pathology.",
        "tests": [
            {
                "name": "FADIR Test (Flexion ADduction Internal Rotation / Impingement Test)",
                "image": "fadir-test.jpg",
                "purpose": "Detect femoroacetabular impingement (FAI) and/or labral pathology",
                "procedure": "The patient lies supine. The examiner passively flexes the hip to approximately 90 degrees, adducts the hip, and internally rotates the hip (bringing the knee toward the contralateral shoulder). This compresses the femoral neck against the acetabular rim.",
                "positive_sign": "Reproduction of deep anterior groin pain. A click or clunk may also be noted. Pain in the lateral hip or buttock is less specific.",
                "sensitivity": 0.99,
                "specificity": 0.06,
                "lr_positive": 1.1,
                "lr_negative": 0.17,
                "notes": "VERY HIGH SENSITIVITY — a negative FADIR effectively rules out FAI/labral pathology. However, very poor specificity — many asymptomatic individuals have a positive FADIR. Use as a screening test (ruling OUT pathology, not ruling it in)."
            },
            {
                "name": "FABER Test (Hip version — Flexion ABduction External Rotation)",
                "image": "faber-test-hip.jpg",
                "purpose": "Provocative test for hip joint pathology (labral tear, FAI, osteoarthritis)",
                "procedure": "The patient lies supine. The examiner places the symptomatic foot on the contralateral knee and applies gentle downward pressure on the ipsilateral knee to stress the hip joint in a position of flexion, abduction, and external rotation.",
                "positive_sign": "Pain reproduced in the groin (anterior hip), limited range, or a capsular end-feel compared to the unaffected side. Lateral/buttock pain is less specific.",
                "sensitivity": 0.41,
                "specificity": 0.76,
                "lr_positive": 1.7,
                "lr_negative": 0.78,
                "notes": "Limited diagnostic accuracy in isolation. Groin pain in FABER suggests intra-articular hip pathology; posterior pain may indicate SIJ or posterior hip involvement. Also used as a measure of hip capsular tightness (distance from lateral knee to table)."
            },
            {
                "name": "Log Roll Test",
                "image": "log-roll-test.jpg",
                "purpose": "Detect intra-articular hip pathology (capsular irritation, loose body, labral tear) by rolling the femoral head within the acetabulum",
                "procedure": "The patient lies supine, relaxed. The examiner grasps the patient's lower leg and gently rolls (internally and externally rotates) the entire limb. This is the LEAST provocative passive movement of the hip (minimal capsular or muscular tension).",
                "positive_sign": "Pain or painful limitation of rotation (particularly internal rotation) compared to the unaffected side. Loss of internal rotation is one of the earliest signs of hip osteoarthritis.",
                "sensitivity": None,
                "specificity": None,
                "lr_positive": None,
                "lr_negative": None,
                "notes": "Because the hip joint is not loaded or moved through a large ROM, any pain reproduction is highly suggestive of intra-articular pathology. Compare the range of internal and external rotation bilaterally."
            },
            {
                "name": "Trendelenburg Test",
                "image": "trendelenburg-test.jpg",
                "purpose": "Assess hip abductor mechanism (gluteus medius and minimus) strength and function",
                "procedure": "The patient stands and is asked to lift one foot off the ground (single-leg stance). The examiner observes the pelvic position from behind. The test can be performed statically (hold for 30 seconds) or dynamically (single-leg squat or step-down).",
                "positive_sign": "A drop (positive Trendelenburg) of the contralateral pelvis (the unsupported side) indicates weak hip abductors on the stance leg. A trunk lean toward the stance side (compensatory) should also be noted.",
                "sensitivity": 0.69,
                "specificity": 0.70,
                "lr_positive": 2.3,
                "lr_negative": 0.44,
                "notes": "Positive Trendelenburg is seen in gluteus medius weakness, hip pathology (OA), superior gluteal nerve injury, or pain-inhibited abductor function. Distinguish between TRUE weakness and PAIN-INHIBITED weakness."
            },
            {
                "name": "Stinchfield Test (Resisted Straight Leg Raise)",
                "image": "stinchfield-test.jpg",
                "purpose": "Detect intra-articular hip pathology using resisted hip flexion to compress the joint",
                "procedure": "The patient lies supine with the symptomatic leg straight. The examiner places a hand on the patient's distal thigh and asks the patient to raise the leg against resistance while the examiner palpates the groin/hip region.",
                "positive_sign": "Pain reproduced in the groin or anterior hip during the resisted effort. This suggests intra-articular pathology (joint compression under load).",
                "sensitivity": 0.83,
                "specificity": 0.15,
                "lr_positive": 1.0,
                "lr_negative": 1.1,
                "notes": "Poor specificity — useful only as a general screening test. Distinguish groin pain (intra-articular) from anterior thigh pain (psoas/extra-articular)."
            },
            {
                "name": "Piriformis Test (FAIR / Freiberg's Test)",
                "image": "piriformis-test.jpg",
                "purpose": "Detect piriformis syndrome (sciatic nerve compression by the piriformis muscle)",
                "procedure": "The patient lies on the unaffected side (side-lying) OR supine. The examiner flexes the symptomatic hip to 60 degrees, adducts it, and internally rotates it (Flexion Adduction Internal Rotation — FAIR position). This stretches the piriformis muscle against the sciatic nerve.",
                "positive_sign": "Reproduction of buttock pain and/or sciatica (posterior thigh/leg pain, tingling, or numbness) with this position. Pain in the buttock alone is less specific.",
                "sensitivity": 0.78,
                "specificity": 0.78,
                "lr_positive": 3.5,
                "lr_negative": 0.28,
                "notes": "Piriformis syndrome is a controversial diagnosis — the test identifies sciatic nerve mechanosensitivity at the piriformis level. Always rule out lumbar radiculopathy as the primary cause of sciatica (SLR, slump test)."
            },
        ]
    },
    "knee": {
        "label": "Knee",
        "description": "The knee is a complex hinge joint with rotational components, relying heavily on ligaments (ACL, PCL, MCL, LCL) and menisci for stability. Common pathologies include ligamentous injuries, meniscal tears, patellofemoral pain, and tendinopathies.",
        "tests": [
            {
                "name": "Lachman's Test",
                "image": "lachmans-test.jpg",
                "purpose": "Assess anterior cruciate ligament (ACL) integrity — the single best test for ACL rupture",
                "procedure": "The patient lies supine with the knee flexed to 20-30 degrees. The examiner stabilises the distal femur with one hand (positioned posteriorly) and grasps the proximal tibia with the other hand. An anteriorly directed force is applied to the tibia while stabilising the femur.",
                "positive_sign": "Excessive anterior translation of the tibia on the femur with a 'soft' or 'mushy' end-feel (compared to a firm, hard end-feel on the intact side). The examiner assesses both the amount of translation and the quality of the endpoint.",
                "sensitivity": 0.87,
                "specificity": 0.93,
                "lr_positive": 12.4,
                "lr_negative": 0.14,
                "notes": "The most sensitive and specific test for ACL rupture. The 20-30 degree position minimises the contribution of secondary stabilisers (hamstrings, menisci, capsule). A negative Lachman in the presence of clinical suspicion warrants further investigation (MRI). Anterior drawer test is less sensitive."
            },
            {
                "name": "Anterior Drawer Test (Knee)",
                "image": "anterior-drawer-knee.jpg",
                "purpose": "Assess ACL integrity (less sensitive than Lachman, useful in acute settings)",
                "procedure": "The patient lies supine with the hip flexed to 45 degrees and the knee flexed to 90 degrees. The examiner sits on the patient's foot to stabilise it and grasps the proximal tibia with both hands, applying an anteriorly directed force.",
                "positive_sign": "Excessive anterior translation of the tibia on the femur compared to the unaffected side. The translation should be graded: Grade I (5mm), Grade II (5-10mm), Grade III (>10mm).",
                "sensitivity": 0.38,
                "specificity": 0.91,
                "lr_positive": 4.2,
                "lr_negative": 0.68,
                "notes": "Less sensitive than Lachman's test in acute injuries due to hamstring guarding and haemarthrosis. However, it is specific and useful in chronic cases. Always compare to the contralateral knee. The position of the foot (neutral, internal, external rotation) can help identify associated meniscal/ligament injuries."
            },
            {
                "name": "Posterior Drawer Test (Knee)",
                "image": "posterior-drawer-knee.jpg",
                "purpose": "Assess posterior cruciate ligament (PCL) integrity — the single best test for PCL rupture",
                "procedure": "The patient lies supine with the hip flexed to 45 degrees and the knee flexed to 90 degrees. The examiner sits on the patient's foot and grasps the proximal tibia with both thumbs on the tibial tuberosity. A posteriorly directed force is applied.",
                "positive_sign": "Excessive posterior translation of the tibia on the femur compared to the unaffected side. A 'sag' of the tibia posteriorly may be visible before any force is applied (posterior sag sign / Godfrey's sign).",
                "sensitivity": 0.90,
                "specificity": 0.99,
                "lr_positive": 90.0,
                "lr_negative": 0.10,
                "notes": "Highest diagnostic accuracy of any knee ligament test. Check for a posterior sag BEFORE performing the test — this alone is highly suggestive of PCL injury. In the presence of a posterior sag, an anterior drawer may be misinterpreted as positive (the tibia is brought from the posteriorly subluxed position to neutral, not anteriorly)."
            },
            {
                "name": "Posterior Sag Sign (Godfrey's / Gravity Test)",
                "image": "posterior-sag-sign.jpg",
                "purpose": "Detect PCL rupture by gravity-induced posterior tibial translation",
                "procedure": "The patient lies supine with both hips and knees flexed to 90 degrees (feet flat on the plinth). The examiner supports the patient's thighs and observes the tibial tuberosity profile from the side.",
                "positive_sign": "The proximal tibia appears to 'sag' posteriorly relative to the unaffected side — the tibial tuberosity is less prominent. This is a gravity-assisted posterior translation of the tibia.",
                "sensitivity": 0.79,
                "specificity": 1.00,
                "lr_positive": None,
                "lr_negative": 0.21,
                "notes": "Highly specific sign of PCL rupture. A visible posterior sag indicates at least a Grade II PCL injury. Always compare bilaterally as some individuals have physiological laxity."
            },
            {
                "name": "Valgus Stress Test (Knee / MCL Test)",
                "image": "valgus-stress-knee.jpg",
                "purpose": "Assess medial collateral ligament (MCL) integrity",
                "procedure": "The patient lies supine. The examiner applies a valgus (abduction) force to the knee while stabilising the ankle/lower leg. The test is performed at 0 degrees (full extension) and 30 degrees of knee flexion.",
                "positive_sign": "Excessive medial joint line opening (gapping) or a soft end-feel. At 0 degrees: gapping suggests involvement of the posteromedial capsule and ACL in addition to the MCL. At 30 degrees: gapping suggests isolated MCL injury.",
                "sensitivity": 0.96,
                "specificity": 0.92,
                "lr_positive": 12.0,
                "lr_negative": 0.04,
                "notes": "Grade by amount of gapping: Grade I (0-5mm), Grade II (5-10mm), Grade III (>10mm). Gapping at 0 degrees indicates more severe injury (multi-ligament involvement). MCL injuries are graded I-III based on gapping and end-feel."
            },
            {
                "name": "Varus Stress Test (Knee / LCL Test)",
                "image": "varus-stress-knee.jpg",
                "purpose": "Assess lateral collateral ligament (LCL) integrity",
                "procedure": "The patient lies supine. The examiner applies a varus (adduction) force to the knee while stabilising the ankle. The test is performed at 0 degrees (full extension) and 30 degrees of knee flexion.",
                "positive_sign": "Excessive lateral joint line gapping or a soft end-feel. At 0 degrees: suggests involvement of lateral capsule and possibly cruciate ligaments. At 30 degrees: more specific for isolated LCL injury.",
                "sensitivity": 0.72,
                "specificity": 0.97,
                "lr_positive": 24.0,
                "lr_negative": 0.29,
                "notes": "LCL injuries are less common than MCL injuries but more likely to be associated with multi-ligament injuries (PLC injury). LCL is part of the posterolateral corner (PLC) — always assess for associated PLC injury."
            },
            {
                "name": "McMurray's Test",
                "image": "mcmurrays-test.jpg",
                "purpose": "Detect meniscal tear (medial and lateral meniscus)",
                "procedure": "The patient lies supine. For the medial meniscus: the examiner fully flexes the knee, then extends it while applying a valgus force and externally rotating the foot. For the lateral meniscus: the examiner extends the knee from flexion while applying a varus force and internally rotating the foot.",
                "positive_sign": "A palpable and/or audible click/clunk along the medial or lateral joint line, combined with reproduction of the patient's pain. A click WITHOUT pain is less clinically significant.",
                "sensitivity": 0.51,
                "specificity": 0.77,
                "lr_positive": 2.2,
                "lr_negative": 0.64,
                "notes": "Poor diagnostic accuracy in isolation — a negative McMurray does NOT rule out a meniscal tear. A positive McMurray (with pain and click) is more useful for ruling in pathology. Thessaly's test at 5 and 20 degrees may be more accurate."
            },
            {
                "name": "Thessaly's Test",
                "image": "thessalys-test.jpg",
                "purpose": "Detect meniscal tear (weight-bearing rotational test, more accurate than McMurray)",
                "procedure": "The patient stands on the affected leg with the knee flexed to 5 degrees, holding the examiner for support. The patient then rotates the body and knee internally and externally (3 times in each direction). The test is repeated at 20 degrees of knee flexion.",
                "positive_sign": "Reproduction of medial or lateral joint line pain, a catching/clicking sensation, or a sense of locking/instability during rotation. The examiner may also feel a click or catch.",
                "sensitivity": 0.89,
                "specificity": 0.86,
                "lr_positive": 6.4,
                "lr_negative": 0.13,
                "notes": "Higher diagnostic accuracy than McMurray's test. The 20-degree position compresses the menisci between the femoral condyles and tibial plateau, making the test more provocative. Contraindicated in acute locked knee or severe pain."
            },
            {
                "name": "Patellar Apprehension Test (Patellar Glide / Lateral Glide)",
                "image": "patellar-apprehension.jpg",
                "purpose": "Assess lateral patellar instability (recurrent patellar dislocation/subluxation)",
                "procedure": "The patient lies supine with the knee relaxed in 20-30 degrees of flexion. The examiner applies a gentle laterally directed force to the patella (pushing it laterally).",
                "positive_sign": "The patient demonstrates apprehension (guarding, grabbing the examiner's hand, facial expression of fear) and asks the examiner to stop. Pain alone without apprehension is NOT a true positive.",
                "sensitivity": 0.47,
                "specificity": 0.93,
                "lr_positive": 6.7,
                "lr_negative": 0.57,
                "notes": "Highly specific — a positive test strongly suggests lateral patellar instability. The same test at 0 degrees (full extension) tests the integrity of the medial patellofemoral ligament (MPFL) in neutral patellar position."
            },
            {
                "name": "Patellar Grind Test (Clarke's Sign / Hoffa's Test)",
                "image": "patellar-grind.jpg",
                "purpose": "Detect patellofemoral joint pathology (chondromalacia patellae, PFJ OA)",
                "procedure": "The patient lies supine with the knee relaxed in extension. The examiner applies direct downward pressure on the patella (compressing it against the femoral trochlea) and asks the patient to contract the quadriceps (or the examiner moves the patella superiorly/inferiorly under compression).",
                "positive_sign": "Pain, crepitus, or a grinding sensation under the patella during compression. The quadriceps contraction loads the patellofemoral joint.",
                "sensitivity": 0.42,
                "specificity": 0.79,
                "lr_positive": 2.0,
                "lr_negative": 0.73,
                "notes": "Poor diagnostic accuracy — a positive test should be interpreted with caution as many asymptomatic individuals have patellofemoral crepitus without pathology. Use as part of a cluster of PFJ tests."
            },
        ]
    },
    "ankle-foot": {
        "label": "Ankle & Foot",
        "description": "The ankle is a highly congruent joint (talocrural) supported by strong lateral and medial ligament complexes. The foot has multiple articulations that provide both mobility and stability. Common pathologies include lateral ankle sprains, syndesmosis injuries, Achilles tendinopathy, and midfoot pathologies.",
        "tests": [
            {
                "name": "Anterior Drawer Test (Ankle)",
                "image": "anterior-drawer-ankle.jpg",
                "purpose": "Assess the integrity of the anterior talofibular ligament (ATFL) — the most commonly injured ankle ligament",
                "procedure": "The patient sits with the knee flexed to 90 degrees (relaxing the gastrocnemius) and the ankle in 10-20 degrees of plantarflexion (neutral position for the ATFL). The examiner stabilises the distal tibia with one hand and grasps the talus/calcaneus with the other, applying an anteriorly directed force.",
                "positive_sign": "Excessive anterior translation of the talus relative to the tibial plafond, a soft end-feel, or reproduction of pain/instability. Compare to the unaffected side.",
                "sensitivity": 0.86,
                "specificity": 0.74,
                "lr_positive": 3.3,
                "lr_negative": 0.19,
                "notes": "Good sensitivity — useful for ruling out ATFL rupture when negative. The ATFL is the most commonly injured ligament in lateral ankle sprains (inversion injury). Always compare bilaterally."
            },
            {
                "name": "Talar Tilt Test (Inversion Stress Test)",
                "image": "talar-tilt.jpg",
                "purpose": "Assess the integrity of the calcaneofibular ligament (CFL) and the lateral ligament complex",
                "procedure": "The patient sits with the knee flexed to 90 degrees and the ankle in neutral position (or slight dorsiflexion to engage the CFL). The examiner stabilises the distal tibia and applies an inversion (varus) tilt to the calcaneus/talus.",
                "positive_sign": "Excessive talar tilt (inversion) compared to the unaffected side, a soft end-feel, or reproduction of pain. The angle of tilt can be estimated: Grade I (<5 deg), Grade II (5-15 deg), Grade III (>15 deg).",
                "sensitivity": 0.66,
                "specificity": 0.90,
                "lr_positive": 6.6,
                "lr_negative": 0.38,
                "notes": "High specificity — a positive test strongly suggests CFL involvement in addition to ATFL. Isolated ATFL injury does NOT produce significant talar tilt. The CFL is the second most commonly injured ligament in lateral ankle sprains."
            },
            {
                "name": "Squeeze Test (Syndesmosis / High Ankle Sprain Test)",
                "image": "squeeze-test.jpg",
                "purpose": "Detect syndesmosis (distal tibiofibular) injury — a 'high ankle sprain'",
                "procedure": "The patient sits with the knee flexed to 90 degrees and the ankle in neutral. The examiner squeezes the tibia and fibula together at the mid-calf (approximately 15-20 cm proximal to the ankle joint).",
                "positive_sign": "Pain is reproduced in the distal syndesmosis area (anterolateral ankle, just proximal to the joint line). Pain in the mid-calf or localised to the squeeze point is not a positive test.",
                "sensitivity": 0.30,
                "specificity": 0.93,
                "lr_positive": 4.3,
                "lr_negative": 0.75,
                "notes": "High specificity but low sensitivity — a positive test strongly suggests syndesmosis injury but a negative test does NOT rule it out. Syndesmosis injuries take significantly longer to heal than lateral ligament sprains."
            },
            {
                "name": "External Rotation Test (Kleiger's Test / Syndesmosis Stress)",
                "image": "external-rotation-ankle.jpg",
                "purpose": "Detect syndesmosis (distal tibiofibular) injury — more sensitive than the Squeeze Test",
                "procedure": "The patient sits with the knee flexed to 90 degrees and the ankle in neutral. The examiner stabilises the distal tibia with one hand and applies an external rotation force to the dorsiflexed foot/ankle.",
                "positive_sign": "Pain reproduced in the syndesmosis region (anterolateral ankle), not in the medial deltoid ligament. Pain may also radiate up the interosseous membrane.",
                "sensitivity": 0.69,
                "specificity": 0.83,
                "lr_positive": 4.1,
                "lr_negative": 0.37,
                "notes": "More sensitive than the Squeeze Test for syndesmosis injury. External rotation of the dorsiflexed foot forces the fibula away from the tibia, stressing the syndesmosis. Compare to the unaffected side."
            },
            {
                "name": "Thompson's Test (Simmonds' / Calf Squeeze Test)",
                "image": "thompsons-test.jpg",
                "purpose": "Detect Achilles tendon rupture (complete tear of the gastrocnemius/soleus complex)",
                "procedure": "The patient lies prone with the feet hanging over the edge of the plinth. The examiner squeezes the calf muscle (gastrocnemius-soleus complex) at the widest point. Normally, squeezing the calf causes passive plantarflexion of the ankle via the intact Achilles.",
                "positive_sign": "Absent or significantly reduced passive plantarflexion when the calf is squeezed. The foot remains in neutral or moves minimally. Compare to the unaffected side.",
                "sensitivity": 0.96,
                "specificity": 0.93,
                "lr_positive": 13.7,
                "lr_negative": 0.04,
                "notes": "Excellent diagnostic accuracy. A positive Thompson's test is highly suggestive of a COMPLETE Achilles tendon rupture. Partial tears may produce a weakly positive or false-negative result. Always perform with the patient prone and knees flexed to 90 degrees to standardise."
            },
            {
                "name": "Matles Test (Knee Flexion Test)",
                "image": "matles-test.jpg",
                "purpose": "Detect Achilles tendon rupture (alternative to Thompson's, useful for large calves)",
                "procedure": "The patient lies prone with both knees actively flexed to 90 degrees (feet pointing toward the ceiling). The examiner observes the position of the feet.",
                "positive_sign": "The foot on the affected side falls into neutral or slight dorsiflexion (compared to the normal side which remains in slight plantarflexion). This indicates loss of the resting tone of the gastrocnemius-soleus complex.",
                "sensitivity": 0.88,
                "specificity": 0.88,
                "lr_positive": 7.3,
                "lr_negative": 0.14,
                "notes": "Useful when Thompson's test is difficult to interpret (e.g. large calf, patient unable to relax). The weight of the foot causes it to drop into dorsiflexion when the tendon is ruptured."
            },
        ]
    },
}

MSK_MUSCLE_TESTS = {
    "shoulder": {
        "label": "Shoulder",
        "description": "Shoulder muscle testing assesses the rotator cuff (SITS: Supraspinatus, Infraspinatus, Teres minor, Subscapularis), deltoid, and scapular stabilisers. The shoulder relies heavily on dynamic muscular control for stability.",
        "movements": [
            {
                "movement": "Shoulder Flexion",
                "image": "shoulder-flexion.jpg",
                "primary_muscle": "Anterior Deltoid",
                "other_muscles": ["Coracobrachialis", "Pectoralis Major (clavicular head)"],
                "nerve_root": "C5, C6",
                "peripheral_nerve": "Axillary Nerve",
                "patient_position": "Seated with arm at side, elbow slightly flexed",
                "stabilization": "Stabilise the scapula and trunk; prevent trunk extension",
                "procedure": "Patient flexes the shoulder forward to 90 degrees (palm facing down). Apply downward resistance at the distal humerus just above the elbow. Palpate the anterior deltoid.",
                "substitutions": "Trunk extension (leaning back), shoulder shrug (upper trap), excessive elbow flexion (biceps)",
                "grades_mmt": {
                    "0": "No palpable contraction",
                    "1": "Palpable contraction in anterior deltoid, no visible movement",
                    "2": "Full ROM gravity-eliminated (side-lying, arm supported on table)",
                    "3": "Full ROM against gravity (seated, arm at side to 90 deg)",
                    "4": "Full ROM against moderate resistance",
                    "5": "Full ROM against maximal resistance"
                }
            },
            {
                "movement": "Shoulder Abduction",
                "image": "shoulder-abduction.jpg",
                "primary_muscle": "Middle Deltoid",
                "other_muscles": ["Supraspinatus (first 0-15 deg)", "Anterior Deltoid", "Serratus Anterior (scapular upward rotation)"],
                "nerve_root": "C5, C6",
                "peripheral_nerve": "Axillary Nerve",
                "patient_position": "Seated with arm at side, elbow slightly flexed",
                "stabilization": "Stabilise the trunk and scapula; prevent trunk side flexion toward the tested side",
                "procedure": "Patient abducts the shoulder to 90 degrees (palm facing down). Apply downward resistance at the distal humerus just above the elbow. Palpate the middle deltoid (lateral shoulder).",
                "substitutions": "Trunk side flexion (leaning away), shoulder elevation (upper trap), external rotation (to use supraspinatus)",
                "grades_mmt": {
                    "0": "No palpable contraction",
                    "1": "Palpable contraction in middle deltoid",
                    "2": "Full ROM gravity-eliminated (supine, arm supported)",
                    "3": "Full ROM against gravity (seated, 0-90 deg)",
                    "4": "Full ROM against moderate resistance",
                    "5": "Full ROM against maximal resistance"
                }
            },
            {
                "movement": "Shoulder External Rotation",
                "image": "shoulder-external-rotation.jpg",
                "primary_muscle": "Infraspinatus",
                "other_muscles": ["Teres Minor", "Posterior Deltoid (accessory)"],
                "nerve_root": "C5, C6 (Infraspinatus — Suprascapular Nerve; Teres Minor — Axillary Nerve)",
                "peripheral_nerve": "Suprascapular Nerve (Infraspinatus)",
                "patient_position": "Seated or prone. For seated: arm at side, elbow flexed to 90 degrees, forearm neutral (mid-position). For prone: shoulder abducted to 90 degrees, elbow flexed to 90 degrees, forearm hanging off the plinth edge.",
                "stabilization": "Stabilise the elbow against the trunk; prevent shoulder abduction or trunk rotation",
                "procedure": "Patient externally rotates the shoulder against resistance applied at the distal forearm (just proximal to the wrist). Palpate the infraspinatus below the spine of the scapula.",
                "substitutions": "Shoulder abduction (posterior deltoid), trunk rotation away from the tested side, elbow extension",
                "grades_mmt": {
                    "0": "No palpable contraction",
                    "1": "Palpable contraction in infraspinatus",
                    "2": "Full ROM gravity-eliminated (prone, arm hanging, gravity-assisted ER)",
                    "3": "Full ROM against gravity (seated, arm at side, ER against gravity)",
                    "4": "Full ROM against moderate resistance",
                    "5": "Full ROM against maximal resistance"
                }
            },
            {
                "movement": "Shoulder Internal Rotation",
                "image": "shoulder-internal-rotation.jpg",
                "primary_muscle": "Subscapularis",
                "other_muscles": ["Pectoralis Major", "Latissimus Dorsi", "Teres Major"],
                "nerve_root": "C5, C6, C7",
                "peripheral_nerve": "Subscapular Nerve (upper and lower) — Subscapularis",
                "patient_position": "Seated or prone. Arm at side, elbow flexed to 90 degrees, forearm neutral. Alternatively, hand behind back (Lift-Off position) for subscapularis isolation.",
                "stabilization": "Stabilise the elbow against the trunk; prevent trunk rotation",
                "procedure": "Patient internally rotates the shoulder against resistance applied at the distal forearm (just proximal to the wrist). Palpate the subscapularis (anterior axillary fold, deep to pectoralis major).",
                "substitutions": "Trunk rotation toward the tested side, shoulder adduction, elbow flexion",
                "grades_mmt": {
                    "0": "No palpable contraction",
                    "1": "Palpable contraction in subscapularis (anterior axilla)",
                    "2": "Full ROM gravity-eliminated",
                    "3": "Full ROM against gravity (seated, IR against gravity)",
                    "4": "Full ROM against moderate resistance",
                    "5": "Full ROM against maximal resistance"
                }
            },
            {
                "movement": "Scapular Retraction (Scapular Adduction)",
                "image": "scapular-retraction.jpg",
                "primary_muscle": "Rhomboids (Major and Minor)",
                "other_muscles": ["Middle Trapezius", "Lower Trapezius (accessory)"],
                "nerve_root": "C4, C5",
                "peripheral_nerve": "Dorsal Scapular Nerve (Rhomboids)",
                "patient_position": "Prone with arm at side or 90 deg abduction, elbow extended",
                "stabilization": "Stabilise the thoracic spine; prevent trunk rotation",
                "procedure": "Patient retracts the scapula (brings shoulder blades together) against resistance applied at the scapula or the arm. Palpate rhomboids between the spine and medial scapular border. Test bilaterally for comparison.",
                "substitutions": "Trunk rotation, shoulder extension (latissimus dorsi), excessive posterior pelvic tilt",
                "grades_mmt": {
                    "0": "No palpable contraction",
                    "1": "Palpable contraction in rhomboids",
                    "2": "Full ROM gravity-eliminated (side-lying, arm supported)",
                    "3": "Full ROM against gravity (prone, arm at side, lift arm/scapula off table)",
                    "4": "Full ROM against moderate resistance",
                    "5": "Full ROM against maximal resistance"
                }
            },
        ]
    },
    "elbow": {
        "label": "Elbow",
        "description": "Elbow muscle testing assesses the elbow flexors (biceps, brachialis, brachioradialis) and extensors (triceps). The elbow also involves the forearm pronators and supinators.",
        "movements": [
            {
                "movement": "Elbow Flexion",
                "image": "elbow-flexion.jpg",
                "primary_muscle": "Biceps Brachii",
                "other_muscles": ["Brachialis", "Brachioradialis"],
                "nerve_root": "C5, C6 (Biceps — Musculocutaneous Nerve; Brachioradialis — Radial Nerve)",
                "peripheral_nerve": "Musculocutaneous Nerve (Biceps Brachii)",
                "patient_position": "Seated with arm at side, forearm supinated (palm up), elbow flexed to 90 degrees",
                "stabilization": "Stabilise the humerus against the trunk; prevent shoulder flexion",
                "procedure": "Patient flexes the elbow against resistance applied at the distal forearm (just proximal to the wrist). Maintain supination throughout to isolate biceps. Palpate the biceps belly.",
                "substitutions": "Shoulder flexion (coracobrachialis/anterior deltoid), forearm pronation (brachialis bias), trunk lean backward",
                "grades_mmt": {
                    "0": "No palpable contraction",
                    "1": "Palpable biceps contraction",
                    "2": "Full ROM gravity-eliminated (arm hanging, gravity-assisted extension)",
                    "3": "Full ROM against gravity (seated, supinated, 0-145 deg)",
                    "4": "Full ROM against moderate resistance",
                    "5": "Full ROM against maximal resistance"
                }
            },
            {
                "movement": "Elbow Extension",
                "image": "elbow-extension.jpg",
                "primary_muscle": "Triceps Brachii",
                "other_muscles": ["Anconeus (accessory extensor)"],
                "nerve_root": "C6, C7, C8",
                "peripheral_nerve": "Radial Nerve",
                "patient_position": "Supine or prone. For supine: shoulder flexed to 90 degrees, elbow fully flexed, forearm pointing upward. For prone: shoulder abducted to 90 degrees, elbow flexed to 90 degrees, forearm hanging off the plinth.",
                "stabilization": "Stabilise the humerus; prevent shoulder movement",
                "procedure": "Patient extends the elbow against resistance applied at the distal forearm (just proximal to the wrist). Palpate the triceps belly (posterior arm).",
                "substitutions": "Shoulder extension (latissimus dorsi, posterior deltoid), trunk lean forward",
                "grades_mmt": {
                    "0": "No palpable contraction",
                    "1": "Palpable triceps contraction",
                    "2": "Full ROM gravity-eliminated (arm supported, gravity-assisted flexion)",
                    "3": "Full ROM against gravity (supine, elbow flexed to extension)",
                    "4": "Full ROM against moderate resistance",
                    "5": "Full ROM against maximal resistance"
                }
            },
            {
                "movement": "Forearm Supination",
                "image": "forearm-supination.jpg",
                "primary_muscle": "Biceps Brachii (with forearm supinated)",
                "other_muscles": ["Supinator Muscle"],
                "nerve_root": "C5, C6 (Biceps — Musculocutaneous; Supinator — Radial/Posterior Interosseous)",
                "peripheral_nerve": "Posterior Interosseous Nerve (Supinator Muscle)",
                "patient_position": "Seated with elbow flexed to 90 degrees, forearm pronated (palm down), arm at side",
                "stabilization": "Stabilise the humerus against the trunk; prevent shoulder internal rotation",
                "procedure": "Patient supinates the forearm (turns palm up) against resistance applied at the distal forearm or a dynamometer. Palpate the supinator (proximal forearm, just distal to radial head).",
                "substitutions": "Shoulder internal rotation, wrist flexion, trunk rotation",
                "grades_mmt": {
                    "0": "No palpable contraction",
                    "1": "Palpable contraction of supinator/biceps",
                    "2": "Full ROM gravity-eliminated (arm hanging, gravity-assisted pronation)",
                    "3": "Full ROM against gravity",
                    "4": "Full ROM against moderate resistance",
                    "5": "Full ROM against maximal resistance"
                }
            },
            {
                "movement": "Forearm Pronation",
                "image": "forearm-pronation.jpg",
                "primary_muscle": "Pronator Teres",
                "other_muscles": ["Pronator Quadratus"],
                "nerve_root": "C6, C7 (Pronator Teres — Median Nerve; Pronator Quadratus — Anterior Interosseous Nerve)",
                "peripheral_nerve": "Median Nerve (Pronator Teres)",
                "patient_position": "Seated with elbow flexed to 90 degrees, forearm supinated (palm up), arm at side",
                "stabilization": "Stabilise the humerus; prevent shoulder external rotation",
                "procedure": "Patient pronates the forearm (turns palm down) against resistance applied at the distal forearm. Palpate the pronator teres (medial proximal forearm).",
                "substitutions": "Shoulder external rotation, wrist extension, shoulder adduction",
                "grades_mmt": {
                    "0": "No palpable contraction",
                    "1": "Palpable contraction of pronator teres",
                    "2": "Full ROM gravity-eliminated (arm hanging, gravity-assisted supination)",
                    "3": "Full ROM against gravity",
                    "4": "Full ROM against moderate resistance",
                    "5": "Full ROM against maximal resistance"
                }
            },
        ]
    },
    "wrist-hand": {
        "label": "Wrist & Hand",
        "description": "Wrist and hand muscle testing assesses the complex interplay of extrinsic and intrinsic muscles that control wrist motion, grip, and fine motor function. Key movements include wrist flexion/extension, finger flexion/extension, and thumb opposition.",
        "movements": [
            {
                "movement": "Wrist Extension",
                "image": "wrist-extension.jpg",
                "primary_muscle": "Extensor Carpi Radialis Longus (ECRL)",
                "other_muscles": ["Extensor Carpi Radialis Brevis (ECRB)", "Extensor Carpi Ulnaris (ECU)"],
                "nerve_root": "C6, C7",
                "peripheral_nerve": "Radial Nerve (Deep Branch) / Posterior Interosseous Nerve",
                "patient_position": "Seated with forearm resting on a table, pronated (palm down), wrist in neutral, fingers relaxed",
                "stabilization": "Stabilise the distal forearm against the table; prevent elbow movement",
                "procedure": "Patient extends the wrist against resistance applied at the dorsum of the hand (metacarpals). Palpate the ECRL/ECRB at the lateral epicondyle and proximal extensor forearm. To isolate ECU, test with the wrist in ulnar deviation.",
                "substitutions": "Finger extension (EDC), elbow flexion, shoulder elevation",
                "grades_mmt": {
                    "0": "No palpable contraction",
                    "1": "Palpable contraction of wrist extensors",
                    "2": "Full ROM gravity-eliminated (forearm supported, gravity-assisted flexion)",
                    "3": "Full ROM against gravity (forearm pronated, wrist hanging off table edge)",
                    "4": "Full ROM against moderate resistance",
                    "5": "Full ROM against maximal resistance"
                }
            },
            {
                "movement": "Wrist Flexion",
                "image": "wrist-flexion.jpg",
                "primary_muscle": "Flexor Carpi Radialis (FCR)",
                "other_muscles": ["Flexor Carpi Ulnaris (FCU)", "Palmaris Longus"],
                "nerve_root": "C6, C7 (FCR — Median Nerve; FCU — Ulnar Nerve)",
                "peripheral_nerve": "Median Nerve (FCR)",
                "patient_position": "Seated with forearm resting on a table, supinated (palm up), wrist in neutral, fingers relaxed",
                "stabilization": "Stabilise the distal forearm; prevent elbow movement",
                "procedure": "Patient flexes the wrist against resistance applied at the palm (thenar/hypothenar eminence). Palpate FCR (medial to palmaris longus at the wrist crease). To isolate FCU, test with the wrist in ulnar deviation.",
                "substitutions": "Finger flexion (FDP/FDS), elbow extension, shoulder internal rotation",
                "grades_mmt": {
                    "0": "No palpable contraction",
                    "1": "Palpable contraction of wrist flexors",
                    "2": "Full ROM gravity-eliminated (forearm supported, gravity-assisted extension)",
                    "3": "Full ROM against gravity (forearm supinated, wrist hanging off table edge)",
                    "4": "Full ROM against moderate resistance",
                    "5": "Full ROM against maximal resistance"
                }
            },
            {
                "movement": "Finger Flexion (Grip Strength)",
                "image": "finger-flexion.jpg",
                "primary_muscle": "Flexor Digitorum Profundus (FDP) — distal phalanx",
                "other_muscles": ["Flexor Digitorum Superficialis (FDS) — middle phalanx", "Lumbricals, Interossei (MCP flexion)"],
                "nerve_root": "C7, C8, T1 (FDP: median to index/middle, ulnar to ring/little; FDS: median nerve)",
                "peripheral_nerve": "Median Nerve (FDP index/middle, FDS) / Ulnar Nerve (FDP ring/little)",
                "patient_position": "Seated with forearm resting supinated on a table",
                "stabilization": "Stabilise the proximal phalanx / metacarpal; prevent wrist flexion",
                "procedure": "For FDP: stabilise the middle phalanx and ask the patient to flex the distal phalanx (DIP joint). For FDS: stabilise the proximal phalanx and ask the patient to flex the middle phalanx (PIP joint) while keeping the other fingers extended. Grip strength can be measured objectively with a hand dynamometer.",
                "substitutions": "Wrist flexion (tenodesis effect), MCP hyperextension (clawing), thumb flexion",
                "grades_mmt": {
                    "0": "No palpable contraction",
                    "1": "Palpable contraction of finger flexors",
                    "2": "Trace movement of the phalanx",
                    "3": "Full ROM against gravity",
                    "4": "Full ROM against moderate resistance",
                    "5": "Full ROM against maximal resistance"
                }
            },
            {
                "movement": "Finger Extension",
                "image": "finger-extension.jpg",
                "primary_muscle": "Extensor Digitorum Communis (EDC)",
                "other_muscles": ["Extensor Indicis Proprius (EIP)", "Extensor Digiti Minimi (EDM)"],
                "nerve_root": "C6, C7, C8",
                "peripheral_nerve": "Radial Nerve → Posterior Interosseous Nerve",
                "patient_position": "Seated with forearm resting pronated on a table, wrist in neutral, fingers flexed",
                "stabilization": "Stabilise the distal forearm; prevent wrist extension",
                "procedure": "Patient extends the fingers (MCP, PIP, DIP joints) against resistance applied at the proximal phalanges (dorsal aspect). Palpate the EDC tendon on the dorsum of the hand. Test EIP (index) and EDM (little) for individual finger extension.",
                "substitutions": "Wrist extension (tenodesis effect), thumb extension, MCP hyperextension with IP flexion (intrinsic minus)",
                "grades_mmt": {
                    "0": "No palpable contraction",
                    "1": "Palpable contraction of EDC",
                    "2": "Full ROM gravity-eliminated",
                    "3": "Full ROM against gravity (fingers extended against gravity)",
                    "4": "Full ROM against moderate resistance",
                    "5": "Full ROM against maximal resistance"
                }
            },
            {
                "movement": "Thumb Opposition",
                "image": "thumb-opposition.jpg",
                "primary_muscle": "Opponens Pollicis",
                "other_muscles": ["Abductor Pollicis Brevis (APB)", "Flexor Pollicis Brevis (FPB)"],
                "nerve_root": "C8, T1",
                "peripheral_nerve": "Median Nerve (Recurrent Motor Branch / Thenar Branch)",
                "patient_position": "Seated with forearm supinated, wrist in neutral, hand relaxed",
                "stabilization": "Stabilise the carpal bones and metacarpals of the hand",
                "procedure": "Patient touches the tip of the thumb to the tip of the little finger (opposition). The examiner applies resistance to the thumb metacarpal, attempting to pull it away from the little finger. Palpate the thenar eminence.",
                "substitutions": "Thumb flexion (FPB — ulnar nerve), wrist flexion, using gravity to assist",
                "grades_mmt": {
                    "0": "No palpable contraction",
                    "1": "Palpable contraction of thenar muscles",
                    "2": "Full ROM gravity-eliminated (hand supinated, gravity-assisted extension)",
                    "3": "Full ROM against gravity (thumb opposes against gravity)",
                    "4": "Full ROM against moderate resistance",
                    "5": "Full ROM against maximal resistance"
                }
            },
        ]
    },
    "cervical": {
        "label": "Cervical Spine",
        "description": "Cervical muscle testing assesses the deep neck flexors (longus colli/capitus), sternocleidomastoid, upper trapezius, and scalenes. Cervical muscle control is critical for head posture, stability, and movement. The deep neck flexors are particularly important in cervicogenic headache and neck pain.",
        "movements": [
            {
                "movement": "Cervical Flexion (Deep Neck Flexors)",
                "image": "cervical-flexion.jpg",
                "primary_muscle": "Longus Colli",
                "other_muscles": ["Longus Capitis", "Sternocleidomastoid (superficial)", "Scalenus Anterior"],
                "nerve_root": "C1-C4",
                "peripheral_nerve": "Ventral Rami of C1-C4 (Cervical Plexus)",
                "patient_position": "Supine with head in neutral (no pillow). The craniocervical flexion test (CCFT) is performed using a pressure biofeedback unit placed under the cervical lordosis.",
                "stabilization": "Stabilise the thoracic spine; prevent excessive chin poking or global cervical flexion",
                "procedure": "Patient performs a gentle head nod (craniocervical flexion — 'chin tuck') without lifting the head off the table. The pressure biofeedback unit measures the ability to isolate the deep neck flexors. Progress to lifting the head off the table (cervical flexion). Maintain the chin tuck throughout.",
                "substitutions": "Chin poking (SCM overactivity), global cervical flexion using SCM/sternum lift, breath holding, jaw clenching",
                "grades_mmt": {
                    "0": "No palpable contraction of deep neck flexors",
                    "1": "Faint contraction, unable to maintain CCFT level 1 (20 mmHg)",
                    "2": "Able to reach CCFT level 2 (22 mmHg) but cannot hold for 10 seconds",
                    "3": "Able to reach and hold CCFT level 3-4 (24-26 mmHg) for 10 seconds",
                    "4": "Able to reach CCFT level 4-5 (26-28 mmHg) and perform full cervical flexion against gravity with good form",
                    "5": "Full cervical flexion with no SCM overactivity, able to hold CCFT level 5 (30 mmHg) for 10 seconds"
                }
            },
            {
                "movement": "Cervical Extension",
                "image": "cervical-extension.jpg",
                "primary_muscle": "Semispinalis Capitis",
                "other_muscles": ["Splenius Capitis", "Splenius Cervicis", "Erector Spinae (cervical/thoracic)", "Upper Trapezius"],
                "nerve_root": "C1-C8 (Dorsal Rami)",
                "peripheral_nerve": "Dorsal Rami of Cervical Spinal Nerves",
                "patient_position": "Prone with head and neck in neutral, forehead resting on the table (or face hole)",
                "stabilization": "Stabilise the upper thoracic spine; prevent scapular elevation",
                "procedure": "Patient extends the head and neck (looks upward) against resistance applied at the occiput. Palpate the suboccipital and paraspinal muscles. Keep the mouth closed and jaw relaxed.",
                "substitutions": "Scapular elevation/shrug (upper trapezius), thoracic extension, jaw clenching",
                "grades_mmt": {
                    "0": "No palpable contraction",
                    "1": "Palpable contraction of cervical extensors, no visible movement",
                    "2": "Full ROM gravity-eliminated (side-lying, head supported)",
                    "3": "Full ROM against gravity (prone, lift head off table)",
                    "4": "Full ROM against moderate resistance",
                    "5": "Full ROM against maximal resistance"
                }
            },
            {
                "movement": "Cervical Lateral Flexion",
                "image": "cervical-lateral-flexion.jpg",
                "primary_muscle": "Sternocleidomastoid (SCM)",
                "other_muscles": ["Scalenes (Anterior, Middle, Posterior)", "Levator Scapulae", "Splenius Cervicis"],
                "nerve_root": "C2-C6 (SCM — Spinal Accessory Nerve C2-C3; Scalenes — Ventral Rami C3-C8)",
                "peripheral_nerve": "Spinal Accessory Nerve (CN XI) — SCM",
                "patient_position": "Supine or seated. Head in neutral, facing forward.",
                "stabilization": "Stabilise the ipsilateral shoulder (prevent shoulder elevation)",
                "procedure": "Patient laterally flexes the head (ear toward shoulder) without rotating or elevating the shoulder. Apply resistance at the temporal region. Palpate the SCM (anterolateral neck) and scalenes (lateral neck).",
                "substitutions": "Shoulder elevation (upper trap), cervical rotation, trunk lateral flexion, cervical extension with rotation",
                "grades_mmt": {
                    "0": "No palpable contraction",
                    "1": "Palpable contraction of SCM/scalenes",
                    "2": "Full ROM gravity-eliminated (supine, head supported, gravity-assisted return)",
                    "3": "Full ROM against gravity (seated, lateral flexion against gravity)",
                    "4": "Full ROM against moderate resistance",
                    "5": "Full ROM against maximal resistance"
                }
            },
            {
                "movement": "Cervical Rotation",
                "image": "cervical-rotation.jpg",
                "primary_muscle": "Sternocleidomastoid (SCM — contralateral rotation)",
                "other_muscles": ["Splenius Capitis (ipsilateral)", "Semispinalis Capitis", "Obliquus Capitis Inferior (atlas-axis rotation)"],
                "nerve_root": "C2-C3 (SCM), C1-C4 (Splenius — Dorsal Rami)",
                "peripheral_nerve": "Spinal Accessory Nerve (CN XI) — SCM",
                "patient_position": "Supine or seated. Head in neutral, facing forward.",
                "stabilization": "Stabilise the shoulders bilaterally; prevent trunk rotation",
                "procedure": "Patient rotates the head (looks to the side) against resistance applied at the ipsilateral temporal/malar region. For SCM testing: patient rotates to the opposite side (e.g., SCM on the right rotates the head to the left). Palpate the contralateral SCM.",
                "substitutions": "Trunk rotation, shoulder rotation, cervical lateral flexion",
                "grades_mmt": {
                    "0": "No palpable contraction",
                    "1": "Palpable contraction of SCM (contralateral)",
                    "2": "Full ROM gravity-eliminated",
                    "3": "Full ROM against gravity (seated, rotation against gravity)",
                    "4": "Full ROM against moderate resistance",
                    "5": "Full ROM against maximal resistance"
                }
            },
        ]
    },
    "lumbar": {
        "label": "Lumbar Spine & SIJ",
        "description": "Lumbar muscle testing assesses the trunk flexors (rectus abdominis, obliques), extensors (erector spinae, multifidus), and lateral flexors (quadratus lumborum). Core/lumbopelvic stability is critical for spinal health and athletic performance.",
        "movements": [
            {
                "movement": "Trunk Flexion (Curl-Up)",
                "image": "trunk-flexion.jpg",
                "primary_muscle": "Rectus Abdominis",
                "other_muscles": ["External Oblique", "Internal Oblique"],
                "nerve_root": "T6-T12 (Intercostal Nerves), L1 (Iliohypogastric)",
                "peripheral_nerve": "Segmental Intercostal Nerves (T6-T12)",
                "patient_position": "Supine with hips and knees flexed to 90 degrees (feet flat on the table), arms crossed over chest",
                "stabilization": "Stabilise the pelvis in a posterior tilt (neutral spine); prevent hip flexor dominance",
                "procedure": "Patient performs a trunk curl-up (lifting the head and shoulders off the table until the inferior scapulae clear the table) — do NOT perform a full sit-up (which primarily uses hip flexors). Palpate the rectus abdominis. Resistance can be applied at the shoulders.",
                "substitutions": "Hip flexion (iliopsoas — the patient 'sits up' using hip flexors instead of curling), neck flexion (chin to chest without trunk curl), posterior pelvic tilt compensation",
                "grades_mmt": {
                    "0": "No palpable contraction",
                    "1": "Palpable rectus abdominis contraction, no trunk movement",
                    "2": "Full curl-up gravity-eliminated (head/shoulders lift, upper back still on table)",
                    "3": "Full curl-up against gravity (scapulae clear the table, arms crossed on chest)",
                    "4": "Full curl-up against moderate resistance (arms behind head, or weight on chest)",
                    "5": "Full curl-up against maximal resistance (weighted, e.g., medicine ball held at chest)"
                }
            },
            {
                "movement": "Trunk Extension (Back Extensors)",
                "image": "trunk-extension.jpg",
                "image2": "trunk-extension1.jpg",
                "primary_muscle": "Erector Spinae (Iliocostalis, Longissimus, Spinalis)",
                "other_muscles": ["Multifidus (deep stabiliser)", "Quadratus Lumborum (lateral trunk)"],
                "nerve_root": "Dorsal Rami of Spinal Nerves (Segmental)",
                "peripheral_nerve": "Dorsal Rami of T1-L5 Spinal Nerves",
                "patient_position": "Prone with arms at sides or behind head, legs stabilised by the examiner or straps",
                "stabilization": "Stabilise the lower body (pelvis and legs); prevent hip extension",
                "procedure": "Patient extends the trunk (lifts the chest off the table) while keeping the hips on the table. Palpate the erector spinae (paraspinal muscles). The Biering-Sorensen Test assesses trunk extensor endurance (hold time in prone with upper body unsupported).",
                "substitutions": "Hip extension (gluteus maximus, hamstrings), leg lifting, scapular retraction (rhomboids/trapezius), neck hyperextension",
                "grades_mmt": {
                    "0": "No palpable contraction",
                    "1": "Palpable erector spinae contraction, no trunk movement",
                    "2": "Full ROM gravity-eliminated (side-lying, trunk extension against gravity eliminated)",
                    "3": "Full ROM against gravity (prone, lift chest off table briefly)",
                    "4": "Full ROM against moderate resistance (arms behind head, lift and hold)",
                    "5": "Full ROM against maximal resistance (weighted, e.g., medicine ball held at chest)"
                }
            },
            {
                "movement": "Trunk Lateral Flexion (Side Bend)",
                "image": "trunk-lateral-flexion.jpg",
                "primary_muscle": "Quadratus Lumborum",
                "other_muscles": ["External Oblique (ipsilateral)", "Internal Oblique (ipsilateral)", "Iliocostalis Lumborum"],
                "nerve_root": "T12-L3",
                "peripheral_nerve": "Subcostal Nerve (T12), Iliohypogastric (L1), Ilioinguinal (L1)",
                "patient_position": "Side-lying (tested side up), legs straight, arm across chest or behind head",
                "stabilization": "Stabilise the pelvis and lower body; prevent trunk rotation or forward/backward lean",
                "procedure": "Patient laterally flexes the trunk (lifts the upper body toward the ceiling) without rotating or flexing forward. Resistance can be applied at the shoulder. Palpate the quadratus lumborum (deep to erector spinae, lateral to lumbar spine).",
                "substitutions": "Trunk rotation, hip hiking (using gluteus medius/TFL instead of QL), pushing with the arm, shoulder elevation",
                "grades_mmt": {
                    "0": "No palpable contraction",
                    "1": "Palpable QL contraction, no trunk movement",
                    "2": "Full ROM gravity-eliminated (supine, side-bending with gravity eliminated by table support)",
                    "3": "Full ROM against gravity (side-lying, lift upper body off table)",
                    "4": "Full ROM against moderate resistance (weight held at shoulder)",
                    "5": "Full ROM against maximal resistance"
                }
            },
        ]
    },
    "hip": {
        "label": "Hip",
        "description": "Hip muscle testing assesses the powerful muscles around the hip joint, including the flexors (iliopsoas), extensors (gluteus maximus, hamstrings), abductors (gluteus medius/minimus), and rotators. The gluteus medius is particularly important for gait and pelvic stability.",
        "movements": [
            {
                "movement": "Hip Flexion",
                "image": "hip-flexion.jpg",
                "primary_muscle": "Iliopsoas (Iliacus and Psoas Major)",
                "other_muscles": ["Rectus Femoris", "Sartorius", "Tensor Fasciae Latae (TFL)"],
                "nerve_root": "L1, L2, L3",
                "peripheral_nerve": "Femoral Nerve (Iliacus, Rectus Femoris) / Ventral Rami L1-L3 (Psoas)",
                "patient_position": "Seated (gravity-eliminated test) or supine (gravity-resisted test). The hip is in neutral, knee relaxed.",
                "stabilization": "Stabilise the pelvis and trunk; prevent posterior pelvic tilt",
                "procedure": "Patient flexes the hip (lifts the thigh upward) against resistance applied at the distal femur (just above the knee). For iliopsoas isolation: keep the knee relaxed (bent) to reduce rectus femoris contribution. Palpate the distal iliopsoas tendon (medial to the sartorius, just distal to the inguinal ligament).",
                "substitutions": "Posterior pelvic tilt (uses abdominal muscles to lift the leg), trunk lean backward, knee extension (rectus femoris dominance)",
                "grades_mmt": {
                    "0": "No palpable contraction of iliopsoas",
                    "1": "Palpable contraction at the inguinal crease, no visible movement",
                    "2": "Full ROM gravity-eliminated (side-lying, hip flexed with gravity eliminated by table)",
                    "3": "Full ROM against gravity (supine, hip flexed to 90 deg against gravity)",
                    "4": "Full ROM against moderate resistance",
                    "5": "Full ROM against maximal resistance"
                }
            },
            {
                "movement": "Hip Extension",
                "image": "hip-extension.jpg",
                "primary_muscle": "Gluteus Maximus",
                "other_muscles": ["Hamstrings (Semitendinosus, Semimembranosus, Biceps Femoris Long Head)", "Adductor Magnus (posterior fibres)"],
                "nerve_root": "L5, S1, S2 (Gluteus Maximus — Inferior Gluteal Nerve)",
                "peripheral_nerve": "Inferior Gluteal Nerve",
                "patient_position": "Prone with hips and knees in neutral (knees extended to isolate gluteus maximus from hamstrings)",
                "stabilization": "Stabilise the pelvis (prevent anterior pelvic tilt / lumbar hyperextension)",
                "procedure": "Patient extends the hip (lifts the leg off the table) while keeping the knee fully extended. Apply resistance at the distal posterior thigh (just above the knee). Palpate the gluteus maximus belly.",
                "substitutions": "Lumbar hyperextension (arching the back — using erector spinae instead of glutes), pelvic rotation, hip external rotation, knee flexion (reducing hamstring length tension)",
                "grades_mmt": {
                    "0": "No palpable contraction in gluteus maximus",
                    "1": "Palpable contraction, no visible movement",
                    "2": "Full ROM gravity-eliminated (side-lying, gravity-assisted flexion)",
                    "3": "Full ROM against gravity (prone, lift leg off table)",
                    "4": "Full ROM against moderate resistance",
                    "5": "Full ROM against maximal resistance"
                }
            },
            {
                "movement": "Hip Abduction",
                "image": "hip-abduction.jpg",
                "primary_muscle": "Gluteus Medius",
                "other_muscles": ["Gluteus Minimus", "Tensor Fasciae Latae (TFL)", "Gluteus Maximus (upper fibres)"],
                "nerve_root": "L4, L5, S1",
                "peripheral_nerve": "Superior Gluteal Nerve",
                "patient_position": "Side-lying (tested side up), legs straight, hip in neutral extension (slight extension to isolate glute med from TFL)",
                "stabilization": "Stabilise the pelvis (prevent posterior pelvic tilt or trunk lean backward)",
                "procedure": "Patient abducts the hip (lifts the leg upward) while keeping the knee fully extended and the foot in neutral (not externally rotated). Apply resistance at the lateral distal femur (just above the lateral knee). Palpate the gluteus medius (superior-lateral buttock, posterior to TFL).",
                "substitutions": "Trunk lateral flexion (side bending away), hip flexion (using TFL instead of glute med), hip external rotation (using piriformis/deep rotators), pelvis hiking (using quadratus lumborum)",
                "grades_mmt": {
                    "0": "No palpable contraction in gluteus medius",
                    "1": "Palpable contraction, no visible movement",
                    "2": "Full ROM gravity-eliminated (supine, legs slide apart on table surface)",
                    "3": "Full ROM against gravity (side-lying, lift leg off table)",
                    "4": "Full ROM against moderate resistance",
                    "5": "Full ROM against maximal resistance"
                }
            },
            {
                "movement": "Hip Adduction",
                "image": "hip-adduction.jpg",
                "primary_muscle": "Adductor Longus",
                "other_muscles": ["Adductor Magnus", "Adductor Brevis", "Pectineus", "Gracilis"],
                "nerve_root": "L2, L3, L4 (Obturator Nerve)",
                "peripheral_nerve": "Obturator Nerve (anterior/posterior divisions)",
                "patient_position": "Side-lying (tested side DOWN), upper leg supported in abduction by examiner or table, lower leg straight",
                "stabilization": "Stabilise the pelvis and the upper leg (prevent pelvic tilt)",
                "procedure": "Patient adducts the lower leg (brings it upward toward the ceiling) or adducts against resistance. Apply resistance at the medial distal femur (just above the medial knee). Palpate the adductor group (medial thigh).",
                "substitutions": "Hip flexion (iliopsoas — brings thigh anteriorly, not medially), trunk side bend (toward tested side), hip internal rotation",
                "grades_mmt": {
                    "0": "No palpable contraction",
                    "1": "Palpable contraction in adductors, no visible movement",
                    "2": "Full ROM gravity-eliminated (supine, leg slides across table)",
                    "3": "Full ROM against gravity (side-lying with tested leg down, lift toward ceiling)",
                    "4": "Full ROM against moderate resistance",
                    "5": "Full ROM against maximal resistance"
                }
            },
            {
                "movement": "Hip External Rotation",
                "image": "hip-external-rotation.jpg",
                "primary_muscle": "Piriformis",
                "other_muscles": ["Gemellus Superior", "Gemellus Inferior", "Obturator Internus", "Obturator Externus", "Quadratus Femoris"],
                "nerve_root": "L4, L5, S1, S2",
                "peripheral_nerve": "Nerve to Piriformis (S1-S2) / Nerve to Obturator Internus (L5-S1) / Nerve to Quadratus Femoris (L4-S1)",
                "patient_position": "Seated with hip and knee flexed to 90 degrees (leg hanging over the edge of the plinth) OR prone with knee flexed to 90 degrees.",
                "stabilization": "Stabilise the thigh and pelvis; prevent hip abduction or trunk rotation",
                "procedure": "Patient externally rotates the hip (foot moves medially) against resistance applied at the medial ankle/distal leg (just above the medial malleolus). Palpate the piriformis (deep in the buttock, posterior to the hip joint).",
                "substitutions": "Hip abduction (the leg drifts outward during ER), posterior pelvic tilt, trunk rotation toward the tested side",
                "grades_mmt": {
                    "0": "No palpable contraction of deep rotators",
                    "1": "Palpable contraction in the gluteal/rotator region",
                    "2": "Full ROM gravity-eliminated (prone, knee flexed, gravity-assisted IR)",
                    "3": "Full ROM against gravity (seated, ER against gravity)",
                    "4": "Full ROM against moderate resistance",
                    "5": "Full ROM against maximal resistance"
                }
            },
        ]
    },
    "knee": {
        "label": "Knee",
        "description": "Knee muscle testing assesses the quadriceps (knee extension) and hamstrings (knee flexion). The quadriceps is the primary knee extensor and a critical muscle for gait, stairs, and sit-to-stand. The hamstrings are important for knee flexion and deceleration.",
        "movements": [
            {
                "movement": "Knee Extension",
                "image": "knee-extension.jpg",
                "primary_muscle": "Quadriceps Femoris (Rectus Femoris, Vastus Lateralis, Vastus Medialis, Vastus Intermedius)",
                "other_muscles": ["Tensor Fasciae Latae (accessory extensor via ITB)"],
                "nerve_root": "L2, L3, L4",
                "peripheral_nerve": "Femoral Nerve",
                "patient_position": "Seated with hip flexed to 90 degrees, knee flexed to 90 degrees, legs hanging off the edge of the plinth",
                "stabilization": "Stabilise the thigh against the table; prevent hip extension or trunk lean backward",
                "procedure": "Patient extends the knee (straightens the leg) against resistance applied at the distal tibia (just above the ankle). Palpate the vastus medialis (VMO) and rectus femoris. For rectus femoris isolation: test with the hip flexed (seated) to put the two-joint rectus on stretch.",
                "substitutions": "Hip extension (leaning back — uses glutes to pull the leg down rather than quads), trunk lean forward (uses momentum), hip external rotation (uses TFL/ITB)",
                "grades_mmt": {
                    "0": "No palpable contraction in quadriceps",
                    "1": "Palpable contraction (patellar tendon tension, VMO contraction visible)",
                    "2": "Full ROM gravity-eliminated (side-lying, leg supported, gravity-assisted flexion)",
                    "3": "Full ROM against gravity (seated, extend knee from 90 deg to full extension)",
                    "4": "Full ROM against moderate resistance",
                    "5": "Full ROM against maximal resistance"
                }
            },
            {
                "movement": "Knee Flexion",
                "image": "knee-flexion.jpg",
                "primary_muscle": "Hamstrings (Semitendinosus, Semimembranosus, Biceps Femoris Long Head)",
                "other_muscles": ["Biceps Femoris Short Head (accessory)", "Gastrocnemius (when knee is extended)", "Sartorius (accessory)", "Gracilis (accessory)"],
                "nerve_root": "L4, L5, S1, S2 (Sciatic Nerve — Tibial Division for all long head hamstrings; Common Peroneal for Biceps Femoris Short Head)",
                "peripheral_nerve": "Sciatic Nerve → Tibial Division",
                "patient_position": "Prone with hips extended, knees flexed to 90 degrees (or fully extended as a starting position). The pelvis should be stabilised.",
                "stabilization": "Stabilise the pelvis and thigh; prevent hip extension or pelvic rotation",
                "procedure": "Patient flexes the knee (brings the heel toward the buttock) against resistance applied at the distal posterior tibia/calcaneus. Palpate the semitendinosus (medial posterior knee) and biceps femoris tendon (lateral posterior knee). To differentiate medial vs lateral hamstrings: test with the foot in internal rotation (medial hamstrings) or external rotation (lateral hamstrings).",
                "substitutions": "Hip extension (gluteus maximus — posterior pelvic tilt helps flex the knee via passive insufficiency), pelvic rotation (rotating the pelvis to assist knee flexion), hip internal rotation",
                "grades_mmt": {
                    "0": "No palpable contraction in hamstrings",
                    "1": "Palpable contraction in hamstring tendons, no movement",
                    "2": "Full ROM gravity-eliminated (side-lying, leg supported, gravity-assisted extension)",
                    "3": "Full ROM against gravity (prone, flex knee from 0 to at least 90 deg against gravity)",
                    "4": "Full ROM against moderate resistance",
                    "5": "Full ROM against maximal resistance"
                }
            },
        ]
    },
    "ankle-foot": {
        "label": "Ankle & Foot",
        "description": "Ankle and foot muscle testing assesses the plantarflexors (gastrocnemius, soleus), dorsiflexors (tibialis anterior), invertors (tibialis posterior), and evertors (peroneals). The ankle musculature is critical for gait, balance, and propulsion.",
        "movements": [
            {
                "movement": "Ankle Plantarflexion",
                "image": "ankle-plantarflexion.jpg",
                "primary_muscle": "Gastrocnemius (with knee extended) / Soleus (with knee flexed)",
                "other_muscles": ["Plantaris", "Flexor Hallucis Longus", "Flexor Digitorum Longus", "Tibialis Posterior"],
                "nerve_root": "S1, S2",
                "peripheral_nerve": "Tibial Nerve",
                "patient_position": "Prone with feet hanging off the edge of the plinth. For gastrocnemius: knee fully extended. For soleus: knee flexed to 90 degrees (reduces gastrocnemius tension).",
                "stabilization": "Stabilise the distal leg; prevent knee flexion (when testing gastrocnemius)",
                "procedure": "Patient plantarflexes the ankle (points the foot) against resistance applied at the plantar surface of the forefoot. Heel raises (single-leg) in standing is a functional test. Palpate the gastrocnemius belly and the Achilles tendon.",
                "substitutions": "Toe curling (FHL/FDL substitute for gastrocnemius/soleus), knee extension (when testing with knee flexed), hip extension, trunk lean forward",
                "grades_mmt": {
                    "0": "No palpable contraction in triceps surae",
                    "1": "Palpable contraction, no visible movement",
                    "2": "Full ROM gravity-eliminated (side-lying, ankle plantarflexes with support)",
                    "3": "Full ROM against gravity (prone, foot hanging, PF through full ROM)",
                    "4": "Full ROM against moderate resistance",
                    "5": "Full ROM against maximal resistance. Single-leg heel raise >20 reps = normal"
                }
            },
            {
                "movement": "Ankle Dorsiflexion",
                "image": "ankle-dorsiflexion.jpg",
                "primary_muscle": "Tibialis Anterior",
                "other_muscles": ["Extensor Hallucis Longus (EHL)", "Extensor Digitorum Longus (EDL)", "Peroneus Tertius"],
                "nerve_root": "L4, L5",
                "peripheral_nerve": "Deep Peroneal Nerve (Fibular Nerve)",
                "patient_position": "Seated or supine with knee flexed to relax gastrocnemius, ankle in neutral (plantargrade)",
                "stabilization": "Stabilise the distal leg; prevent knee extension or hip flexion",
                "procedure": "Patient dorsiflexes the ankle (brings foot/toes upward) against resistance applied at the dorsal forefoot. To isolate tibialis anterior: combine dorsiflexion with inversion. Palpate the tibialis anterior muscle belly (anterolateral shin).",
                "substitutions": "Toe extension (EDL/EHL used instead of TA), knee extension (gastrocnemius length-tension change), hip flexion with leg lift",
                "grades_mmt": {
                    "0": "No palpable contraction of tibialis anterior",
                    "1": "Palpable contraction, no visible movement",
                    "2": "Full ROM gravity-eliminated (side-lying, foot supported, gravity-assisted PF)",
                    "3": "Full ROM against gravity (seated/supine, DF against gravity)",
                    "4": "Full ROM against moderate resistance",
                    "5": "Full ROM against maximal resistance"
                }
            },
            {
                "movement": "Ankle Eversion",
                "image": "ankle-eversion.jpg",
                "primary_muscle": "Peroneus Longus",
                "other_muscles": ["Peroneus Brevis", "Peroneus Tertius"],
                "nerve_root": "L4, L5, S1",
                "peripheral_nerve": "Superficial Peroneal Nerve (Fibular Nerve)",
                "patient_position": "Side-lying (tested side up) or seated with the knee flexed and ankle in neutral",
                "stabilization": "Stabilise the distal leg; prevent hip or knee movement",
                "procedure": "Patient everts the foot (turns the sole outward) against resistance applied at the lateral border of the foot (5th metatarsal). Palpate the peroneal tendons behind the lateral malleolus and the peroneus brevis/longus muscle bellies on the lateral shin.",
                "substitutions": "Ankle plantarflexion (peroneals also PF the ankle — PF may substitute for pure eversion), hip external rotation, lateral trunk lean, ankle dorsiflexion (peroneus tertius)",
                "grades_mmt": {
                    "0": "No palpable contraction of peroneals",
                    "1": "Palpable contraction in peroneal tendons",
                    "2": "Full ROM gravity-eliminated (supine, foot supported, gravity-assisted inversion)",
                    "3": "Full ROM against gravity (side-lying, foot everted against gravity)",
                    "4": "Full ROM against moderate resistance",
                    "5": "Full ROM against maximal resistance"
                }
            },
            {
                "movement": "Ankle Inversion",
                "image": "ankle-inversion.jpg",
                "primary_muscle": "Tibialis Posterior",
                "other_muscles": ["Tibialis Anterior (accessory inverter)", "Flexor Digitorum Longus", "Flexor Hallucis Longus"],
                "nerve_root": "L4, L5 (Tibialis Posterior — Tibial Nerve)",
                "peripheral_nerve": "Tibial Nerve",
                "patient_position": "Side-lying (tested side down) or seated with the knee flexed and ankle in neutral",
                "stabilization": "Stabilise the distal leg; prevent hip or knee movement",
                "procedure": "Patient inverts the foot (turns the sole inward) against resistance applied at the medial border of the foot (1st metatarsal/navicular). Palpate the tibialis posterior tendon (behind the medial malleolus) and the muscle belly (deep posterior compartment, posteromedial shin).",
                "substitutions": "Ankle plantarflexion (TP is also a PF — PF may be substituted for pure inversion), dorsiflexion plus inversion (TA substitution), hip internal rotation",
                "grades_mmt": {
                    "0": "No palpable contraction of tibialis posterior",
                    "1": "Palpable contraction in TP tendon behind medial malleolus",
                    "2": "Full ROM gravity-eliminated (supine, foot supported, gravity-assisted eversion)",
                    "3": "Full ROM against gravity (side-lying with tested side down, foot inverted against gravity)",
                    "4": "Full ROM against moderate resistance",
                    "5": "Full ROM against maximal resistance"
                }
            },
        ]
    },
}
