DEFAULT_CFG = {
    "config": {"include": [],},
    "job": {
        "job_name": "JOB_NAME_DEF",
        "job_type": "JOB_TYPE_DEF",
        "save_dir": ".",
        "load_job_name": "LOAD_JOB_NAME_DEF",
        "fix_rdm_seed": True,
        "rdm_seed": 1024,
    },
    "input": {
        "norm_array": True,
        "feature_norm_alias": {},
        "sig_sumofweight": 1000,
        "bkg_sumofweight": 1000,
        "data_sumofweight": 1000,
        "reset_feature": False,
        "reset_feature_name": "RESET_FEATURE_NAME_DEF",
        "rm_negative_weight_events": False,
        "arr_path": "",
        "arr_version": "",
        "variation": "",
        "campaign": "",
        "region": "",
        "channel": "",
        "sig_key": "all",
        "sig_list": [],
        "bkg_key": "all",
        "bkg_list": [],
        "selected_features": [],
        "validation_features": [],
        "cut_features": [],
        "cut_values": [],
        "cut_types": [],
    },
    "train": {
        "model_name": "MODEL_NAME_DEF",
        "model_class": "Model_Sequential_Flat",
        "output_bkg_node_names": [],
        "layers": 1,
        "nodes": 1,
        "learn_rate": 0.01,
        "learn_rate_decay": 0.01,
        "batch_size": 32,
        "epochs": 1,
        "momentum": 0,
        "nesterov": False,
        "dropout_rate": 0,
        "sig_class_weight": 1,
        "bkg_class_weight": 1,
        "test_rate": 0.2,
        "val_split": 0.25,
        "k_folds": None,
        "use_early_stop": False,
        "early_stop_paras": {
            "monitor": "val_loss",
            "min_delta": 0,
            "patience": 1,
            "mode": "min",
            "restore_best_weights": True,
        },
        "train_metrics": [],
        "train_metrics_weighted": ["accuracy"],
        "save_model": True,
        "verbose": 0,
    },
    "apply": {
        "check_model_epoch": False,
        "book_history": False,
        "cfg_history": {},
        "book_roc": False,
        "book_mva_scores_data_mc": False,
        "cfg_mva_scores_data_mc": {
            "sig_list": [],
            "bkg_list": [],
            "apply_data": False,
            "data_key": "",
            "apply_data_range": None,
            "plot_title": "MVA scores",
            "bins": 25,
            "range": [0, 1],
            "density": False,
            "log": False,
            "save_format": "png",
            "use_root": False,
        },
        "book_train_test_compare": False,
        "cfg_train_test_compare": {
            "sig_key": None,
            "bkg_key": None,
            "plot_title": "train/test MVA scores compare",
            "bins": 25,
            "range": [0, 1],
            "density": False,
            "log": False,
            "save_format": "png",
        },
        "book_kine_study": False,
        "book_cut_kine_study": False,
        "cfg_kine_study": {
            "separate_sig_bkg": False,  # only valid for no DNN cut kinematics
            "save_ratio_table": False,  # only valid for DNN cut kinematics
            "bins": 40,
            "range": None,
            "histtype": "stepfilled",
            "alpha": 0.3,
            "density": False,
            "sig_color": "tomato",
            "bkg_color": "royalblue",
            "dnn_cut_list": None,
            "save_format": "png",
        },
        "book_cor_matrix": False,
        "book_importance_study": False,
        "book_significance_scan": False,
        "cfg_significance_scan": {"significance_algo": "s_sqrt_b_rel",},
        "book_fit_npy": False,
        "cfg_fit_npy": {
            "fit_npy_region": "",
            "fit_npy_branches": [],
            "npy_save_dir": "",
        },
    },
    "para_scan": {"perform_para_scan": False,},
    "run": {
        "datestr": "",
        "npy_path": "",
        "config_collected": False,
        "input_dim": None,
    },
}
